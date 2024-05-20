#!/bin/bash
# Update all dependencies and pin them to requirements.txt.

# Run the following for a clean install.
# pip freeze | xargs pip uninstall -y

pip install jupyterlab pyright
pip install beautifulsoup4 discord.py requests
pip freeze >Requirements.txt
