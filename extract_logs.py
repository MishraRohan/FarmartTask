import os
import sys
from datetime import datetime

# Directory to store the output files
OUTPUT_DIR = "output"

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to filter logs by a specific date
def filter_logs_by_date(log_file_path, target_date):
    filtered_logs = []

    # Open the log file for reading
    with open(log_file_path, "r") as log_file:
        for line in log_file:
            # Extract the date part from the log entry (YYYY-MM-DD format)
            log_date = line.split(' ')[0]

            # If the log entry matches the target date, add it to the filtered list
            if log_date == target_date:
                filtered_logs.append(line.strip())  # Strip to remove any extra newlines

    return filtered_logs

# Function to save filtered logs to a new file
def save_filtered_logs(filtered_logs, target_date):
    # Create a file name for the output file
    output_file_path = os.path.join(OUTPUT_DIR, f"output_{target_date}.txt")

    # Save the filtered logs to the output file
    with open(output_file_path, "w") as output_file:
        for log in filtered_logs:
            output_file.write(log + "\n")

    print(f"Filtered logs saved to {output_file_path}")

# Main function to execute the filtering process
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <YYYY-MM-DD>")
        sys.exit(1)

    # Get the target date from the command-line argument
    target_date = sys.argv[1]

    # Validate the date format
    try:
        datetime.strptime(target_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    # Path to the log file
    log_file_path = "src/log_file.txt"  # Assuming the logs are in src/log_file.txt

    # Filter the logs by the target date
    filtered_logs = filter_logs_by_date(log_file_path, target_date)

    # If no logs were found for the given date
    if not filtered_logs:
        print(f"No logs found for {target_date}.")
        sys.exit(1)

    # Save the filtered logs to the output directory
    save_filtered_logs(filtered_logs, target_date)

if __name__ == "__main__":
    main()
