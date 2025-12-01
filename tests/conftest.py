import pytest
from click.testing import CliRunner
from unittest import mock
import subprocess
import os

@pytest.fixture
def runner():
    """A Click CliRunner instance for invoking the CLI commands."""
    return CliRunner()

@pytest.fixture
def mock_subprocess_run():
    """Mocks subprocess.run to record calls and simulate success."""
    with mock.patch('subprocess.run') as mocked_run:
        # Configure the mock to always succeed (return code 0)
        mocked_run.return_value = mock.Mock(returncode=0)
        yield mocked_run

@pytest.fixture(autouse=True)
def mock_compose_file_exists():
    """Mocks os.path.exists to confirm the compose file is present."""
    with mock.patch('os.path.exists', return_value=True) as mock_exists:
        yield mock_exists