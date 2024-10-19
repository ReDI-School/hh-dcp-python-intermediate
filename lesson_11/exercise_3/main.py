import os
import time

def watch_directory(directory):
    seen_files = set(os.listdir(directory))
    print(f"Watching directory: {directory}")

    while True:
        current_files = set(os.listdir(directory))
        new_files = current_files - seen_files

        for new_file in new_files:
            print(f"New file created: {new_file}")

        seen_files = current_files
        time.sleep(2)  # Pause for 2 seconds

if __name__ == "__main__":
    watch_directory("/path/to/directory")