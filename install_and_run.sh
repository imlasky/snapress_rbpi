#!/bin/bash

# Check if the run_script_pid.txt file exists
if [ -e run_script_pid.txt ]; then
    # Read the PID from the file
    pid=$(cat run_script_pid.txt)

    # Kill the existing process
    kill $pid
    rm run_script_pid.txt  # Remove the PID file
    echo "Background process stopped."
fi

# Create a virtual environment (if not already created)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # Assuming the virtual environment is in the 'venv' directory

# Install packages from requirements.txt
pip install -r requirements.txt

# Prompt user for email and password
read -p "Enter your email: " email
echo  # Add a newline
read -s -p "Enter your password: " password
echo  # Add a newline

# Save email and password to .env file
echo "EMAIL=$email" > .env
echo "PASSWORD=$password" >> .env

# Get a list of printers and let the user choose one
echo "Available printers:"
lpstat -p -d | awk '/printer/ {print NR, $2}'
read -p "Enter the number of your preferred printer: " printer_number

# Get the printer name based on the selected number
printer_name=$(lpstat -p -d | awk -v n="$printer_number" 'NR==n {print $2}')

# Set the preferred printer as the default printer using lpoptions
lpoptions -d "$printer_name" > /dev/null 2>&1 && echo "Default printer set"

# Run the run_script.sh in the background and save the PID to a file
./run_script.sh &

# Save the PID to a file
echo $! > run_script_pid.txt