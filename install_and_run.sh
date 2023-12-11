#!/bin/bash

# Create a virtual environment (if not already created)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # Assuming the virtual environment is in the 'venv' directory

# Install packages from requirements.txt
pip install -r requirements.txt

# Prompt user for email and password
read -p "Enter your email: " email
read -s -p "Enter your password: " password

# Save email and password to .env file
echo "EMAIL=$email" > .env
echo "PASSWORD=$password" >> .env

# Run the run_script.sh in the background
./run_script.sh &