#!/bin/bash

# define script name
SCRIPT_NAME=$(basename "$0")

# nuke everything except this script
find . -mindepth 1 ! -name "$SCRIPT_NAME" -exec rm -rf {} + 2>/dev/null

# make folder structure
mkdir -p app db data

# recreate blank project files
touch docker-compose.yml Dockerfile requirements.txt .env

# app-level Python files
touch app/__init__.py
touch app/dashboard.py
touch app/collect_gilts.py
touch app/db_connection.py
touch app/fred_client.py
touch app/gilt_yield_client.py
touch app/kaggle_client.py
touch app/ons_client.py
touch app/init_db.py

# optional: placeholders in db or data
touch db/.gitkeep
touch data/.gitkeep

echo "reset complete. folder structure and blank files created."

