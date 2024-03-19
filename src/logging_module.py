import datetime
import os


def create_log_file():
    current_dir = os.getcwd()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"log_{timestamp}.txt"
    log_file_path = os.path.join(current_dir, filename)
    with open(log_file_path, 'w') as file:
        pass
    return log_file_path

def write_log(message, log_file_path):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file_path, 'a') as file:
            file.write(f"{timestamp} - {message}\n")
    except Exception as e:
        print(f"Failed to write to log file: {e}")

def log_error(error_message, log_file_path):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file_path, 'a') as file:
            file.write(f"{timestamp} - ERROR - {error_message}\n")
    except Exception as e:
        print(f"Failed to write to log file: {e}")
