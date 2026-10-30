import argparse
import os
from datetime import datetime


def get_file_timestampe(file_path):
    return os.path.getmtime(file_path)

def main():
    parser = argparse.ArgumentParser(description="Get the timestamp of a file.")
    parser.add_argument("file_path", help="Path to the file")
    args = parser.parse_args()
 
    file_path = args.file_path
    print(f"Checking timestamp for file: {file_path}")
    if os.path.exists(file_path):
        formatted = datetime.fromtimestamp(get_file_timestampe(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Timestamp for {file_path}: {formatted}")
    else:
        print(f"File {file_path} does not exist.")

if __name__ == "__main__":
    main()