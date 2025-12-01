#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

VENV_DIR=".venv"
BACKEND_REQS="backend/requirements.txt"
ROOT_REQS="requirements.txt"

echo "--- MSRV Development Environment Setup ---"

# Check for and create the virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR..."
    python -m venv "$VENV_DIR"
    echo "Virtual environment created successfully."
else
    echo "Virtual environment ($VENV_DIR) already exists. Skipping creation."
fi

# Determine the Python executable path within the new/existing venv
PYTHON_EXEC="$VENV_DIR/bin/python"

# Install root dependencies (if they exist)
if [ -f "$ROOT_REQS" ]; then
    echo "Installing root dependencies from $ROOT_REQS..."
    "$PYTHON_EXEC" -m pip install -r "$ROOT_REQS"
else
    echo "ERROR: Root requirements file ($ROOT_REQS) not found!"
    exit 1
fi

# Install backend dependencies (must exist)
if [ -f "$BACKEND_REQS" ]; then
    echo "Installing backend dependencies from $BACKEND_REQS..."
    "$PYTHON_EXEC" -m pip install -r "$BACKEND_REQS"
else
    echo "ERROR: Backend requirements file ($BACKEND_REQS) not found!"
    exit 1
fi

# Host File Registration
echo "Attempting to register msrv.local.com in /etc/hosts..."
echo "If this is your first run, you will be prompted for your SUDO password."

# Execute the registration CLI command using the installed venv Python
"$PYTHON_EXEC" msrv.py register-hosts

echo ""
echo "#####################################################"
echo "#  FINAL STEP: Activate your Virtual Environment!   #"
echo "#####################################################"
echo "To start working, run the following command:"
echo ""
echo "  source .venv/bin/activate"
echo ""