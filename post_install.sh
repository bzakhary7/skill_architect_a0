#!/bin/bash
PYTHON_EXEC=$1
PLUGIN_DIR=$2

cd "$PLUGIN_DIR"
VENV_DIR="$PLUGIN_DIR/python_deps"

# Install python dependencies to local python_deps folder
$PYTHON_EXEC -m pip install -r requirements.txt --target "$VENV_DIR" --upgrade
