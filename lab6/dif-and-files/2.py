import os

def check_path_access(path):
    print(f"Checking path: {path}")
    print("Exists:", os.access(path, os.F_OK))  # Check existence
    print("Readable:", os.access(path, os.R_OK))  # Check read permission
    print("Writable:", os.access(path, os.W_OK))  # Check write permission
    print("Executable:", os.access(path, os.X_OK))  # Check execute permission

# Get user input for the path
user_path = input("Enter the path: ")
check_path_access(user_path)
