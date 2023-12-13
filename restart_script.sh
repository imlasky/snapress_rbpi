# Log file path
log_file="install_and_run.log"

# Function to log errors
log_error() {
    echo "[ERROR] $1" >> "$log_file"
}

# Check if the run_script_pid.txt file exists
if [ -e run_script_pid.txt ]; then
    # Read the PID from the file
    pid=$(cat run_script_pid.txt)

    # Kill the existing process
    kill $pid
    rm run_script_pid.txt  # Remove the PID file
    echo "background process stopped."
fi

# Run the run_script.sh in the background and save the PID to a file
./run_script.sh >> "$log_file" 2>&1 &