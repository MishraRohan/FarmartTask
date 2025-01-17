import os
import random
import string
from datetime import datetime, timedelta

# Directory to store the log files (saving to 'src')
LOG_DIR = "src"

# Create the directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Function to generate a random log entry with an increasing timestamp
def generate_log_entry(current_time):
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(["INFO", "WARNING", "ERROR"])
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    return f"{timestamp} [{log_level}] {message}"

# Function to generate logs for multiple days with increasing timestamps
def generate_logs_for_multiple_days(start_date, end_date, num_entries_per_day=1000):
    logs = []
    current_date = start_date
    current_time = datetime.combine(current_date, datetime.min.time())
    
    while current_date <= end_date:
        for _ in range(num_entries_per_day):
            log = generate_log_entry(current_time)
            logs.append(log)
            # Increment the time by a random number of seconds for each log entry to ensure increasing timestamps
            current_time += timedelta(seconds=random.randint(10, 120))
        
        current_date += timedelta(days=1)  # Move to the next day
        current_time = datetime.combine(current_date, datetime.min.time())  # Reset to start of the next day
    
    return logs

# Function to save logs to a file
def save_logs_to_file(logs):
    filename = f"{LOG_DIR}/log_file.txt"  # Save to 'src/log_file.txt'
    with open(filename, "w") as f:
        for log in logs:
            f.write(log + "\n")
    print(f"Logs saved to {filename}")

# Generate logs for the date range from 2025-01-01 to 2025-01-10
if __name__ == "__main__":
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 1, 10)
    print(f"Generating logs from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    logs = generate_logs_for_multiple_days(start_date, end_date, num_entries_per_day=1000)
    save_logs_to_file(logs)
