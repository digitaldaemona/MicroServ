import subprocess
from msrv import cli


def test_up_command(runner, mock_subprocess_run):
    """Verify that 'msrv up' executes the correct docker compose command."""
    
    result = runner.invoke(cli, ['up'])
    assert result.exit_code == 0
    mock_subprocess_run.assert_called_once()
    expected_command = "docker compose -f docker-compose.yml up --build -d"
    assert mock_subprocess_run.call_args[0][0] == expected_command

def test_down_command(runner, mock_subprocess_run):
    """Verify that 'msrv down' executes the correct docker compose down command."""
    
    result = runner.invoke(cli, ['down'])
    assert result.exit_code == 0
    mock_subprocess_run.assert_called_once()
    expected_command = "docker compose -f docker-compose.yml down --volumes"
    assert mock_subprocess_run.call_args[0][0] == expected_command

def test_up_command_failure(runner, mock_subprocess_run):
    """Verify that 'msrv up' handles a failure in the underlying Docker command."""
    
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, 'mocked command')
    result = runner.invoke(cli, ['up'])
    assert result.exit_code == 1
    assert "ERROR: Failed to start services." in result.output