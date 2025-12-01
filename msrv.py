#!/usr/bin/env python

from typing import Tuple
import click
import subprocess
import sys
import os
from dotenv import load_dotenv

load_dotenv()

MSRV_LOCAL_DOMAIN = 'msrv.local.com'
HOSTS_FILE = '/etc/hosts'
LOCAL_IP = '127.0.0.1'
DEV_COMPOSE_FILE = 'docker-compose.dev.yml'
PROD_COMPOSE_FILE = 'docker-compose.prod.yml'
SWARM_STACK_NAME = 'msrv_app'

def run_command(command: str, error_message: str, remote=False) -> None:
    """Executes a shell command and handles errors."""
    if remote:
        click.echo(click.style(f"REMOTE EXEC: {command}", fg='cyan'))
    else:
        click.echo(click.style(f"LOCAL EXEC: {command}", fg='cyan'))

    try:
        # shell=True allows us to pass the full string command (e.g. SSH)
        subprocess.run(command, check=True, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    except subprocess.CalledProcessError as e:
        click.echo(click.style(f"\nERROR: {error_message}", fg='red'))
        click.echo(click.style(f"Command returned exit code {e.returncode}", fg='red'))
        sys.exit(e.returncode)

def get_prod_config() -> Tuple[str, str, str | None]:
    """Loads SSH details and constructs the identity flag safely."""
    ssh_user = os.getenv("SSH_USER") or ""
    ssh_host = os.getenv("SSH_HOST") or ""
    raw_key_path = os.getenv("PEM_KEY_PATH") 
    
    if not all([ssh_user, ssh_host]):
        raise click.UsageError("Production deployment requires SSH_USER and SSH_HOST in .env")
    
    identity_flag = ""
    if raw_key_path:
        full_key_path = os.path.expanduser(raw_key_path)
        
        if not os.path.exists(full_key_path):
             raise click.UsageError(f"PEM Key not found at: {full_key_path}")
             
        identity_flag = f"-i \"{full_key_path}\""

    return ssh_user, ssh_host, identity_flag

def add_hosts_entry(hostname: str) -> None:
    """Adds a hostname entry to the /etc/hosts file if it doesn't exist."""
    entry = f"{LOCAL_IP}\t{hostname}"
    
    try:
        # Check if the entry already exists
        with open(HOSTS_FILE, 'r') as f:
            if hostname in f.read():
                click.echo(f"Host entry for '{hostname}' already exists. Skipping.")
                return

        # If it doesn't exist, use sudo and tee to append the entry
        click.echo(click.style(f"Adding '{hostname}' to {HOSTS_FILE}. This may require sudo.", fg='yellow'))
        
        # Using tee ensures the file is appended safely with sudo
        command = f"echo '{entry}' | sudo tee -a {HOSTS_FILE}"
        
        # Running it directly here handles the sudo prompt better.
        subprocess.run(command, shell=True, check=True)
        
        click.echo(click.style(f"Successfully added {hostname}.", fg='green'))

    except subprocess.CalledProcessError:
        click.echo(click.style("\nERROR: Failed to update hosts file.", fg='red'))
        click.echo(click.style("Please run the script with necessary permissions or add the entry manually.", fg='red'))
        sys.exit(1)
    except FileNotFoundError:
        click.echo(click.style(f"Error: {HOSTS_FILE} not found. Are you on Linux/macOS?", fg='red'))
        sys.exit(1)

@click.group()
def cli():
    """Microservice (MSRV) Management CLI"""
    pass

@cli.command()
@click.argument('hostname', default=MSRV_LOCAL_DOMAIN, required=False)
def register_hosts(hostname):
    """Registers a local development domain (default: msrv.local.com) in /etc/hosts."""
    click.echo(click.style("--- Host Registration Utility ---", fg='blue'))
    add_hosts_entry(hostname)

@cli.command()
@click.option('--prod', is_flag=True, help='Deploy to remote production server via Swarm.')
def up(prod: bool) -> None:
    """Start services (Local Docker Compose or Remote Swarm)."""
    if prod:
        try:
            ssh_user, ssh_host, identity_flag = get_prod_config()
        except click.UsageError as e:
            click.echo(click.style(e.message, fg='red')); sys.exit(1)

        compose_file = PROD_COMPOSE_FILE
        if not os.path.exists(compose_file):
            click.echo(click.style(f"Error: {compose_file} missing.", fg='red')); sys.exit(1)

        click.echo(click.style(f"Deploying to {ssh_user}@{ssh_host}...", fg='blue'))
        
        # SCP the compose file
        scp_cmd = f"scp {identity_flag} \"{compose_file}\" {ssh_user}@{ssh_host}:/tmp/{compose_file}"
        run_command(scp_cmd, "SCP transfer failed.")
        
        # SSH and Deploy Stack
        ssh_prefix = f"ssh {identity_flag} {ssh_user}@{ssh_host}"
        
        # Docker Swarm Init
        check_swarm_cmd = (
            "if [ \"$(docker info --format '{{.Swarm.LocalNodeState}}')\" != \"active\" ]; then "
            "docker swarm init; "
            "else echo 'Swarm is already active'; fi"
        )
        run_command(f"{ssh_prefix} '{check_swarm_cmd}'", "Swarm init check failed.", remote=True)

        # Deploy
        deploy_cmd = f"{ssh_prefix} 'docker stack deploy -c /tmp/{compose_file} {SWARM_STACK_NAME} --with-registry-auth'"
        run_command(deploy_cmd, "Stack deploy failed.", remote=True)
        
        click.echo(click.style("\nDeployment successful.", fg='green'))
    else:
        # Local Dev
        if not os.path.exists(DEV_COMPOSE_FILE):
            click.echo(click.style(f"Error: {DEV_COMPOSE_FILE} missing.", fg='red')); sys.exit(1)
        
        click.echo(click.style("Starting local dev environment...", fg='green'))
        run_command(f"docker compose -f {DEV_COMPOSE_FILE} up --build -d", "Local up failed.")
        click.echo(click.style("\nLocal Dev running at http://msrv.local.com", fg='green'))

@cli.command()
@click.option('--prod', is_flag=True, help='Remove remote production stack.')
def down(prod) -> None:
    """Stop services and clean up."""
    if prod:
        try:
            ssh_user, ssh_host, identity_flag = get_prod_config()
        except click.UsageError as e:
            click.echo(click.style(e.message, fg='red')); sys.exit(1)
            
        click.echo(click.style(f"Removing remote stack...", fg='yellow'))
        ssh_prefix = f"ssh {identity_flag} {ssh_user}@{ssh_host}"
        run_command(f"{ssh_prefix} 'docker stack rm {SWARM_STACK_NAME}'", "Stack removal failed.", remote=True)
        click.echo(click.style("\nRemote stack removed.", fg='green'))
    else:
        click.echo(click.style("Stopping local dev and removing volumes...", fg='yellow'))
        run_command(f"docker compose -f {DEV_COMPOSE_FILE} down --volumes", "Local down failed.")
        click.echo(click.style("\nLocal cleanup complete.", fg='yellow'))

if __name__ == '__main__':
    cli()