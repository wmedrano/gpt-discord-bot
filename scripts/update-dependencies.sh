#!/bin/bash
# Update all dependencies and pin them to requirements.txt.

pip freeze | xargs pip uninstall -y
pip install discord.py
pip freeze >Requirements.txt
