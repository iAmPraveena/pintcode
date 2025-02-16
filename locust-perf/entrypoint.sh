#!/bin/sh

# Ensure the virtual environment is activated
source /usr/local/venv/bin/activate

# Run the Locust command passed as arguments
exec "$@"

