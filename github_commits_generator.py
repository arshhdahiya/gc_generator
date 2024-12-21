import os
import random
from datetime import datetime, timedelta
import subprocess
import sys
import ctypes

def is_admin():
    """Check if the script is run as an administrator."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking for admin privileges: {e}")
        return False

def change_system_date(new_date):
    """Change the system date to the specified new_date (MM-DD-YYYY)."""
    if not is_admin():
        print("You need to run this script as an administrator.")
        sys.exit(1)

    try:
        # Construct the command to change the system date (format: MM-DD-YYYY)
        command = f'date {new_date}'

        # Execute the command to change the system date
        subprocess.run(command, check=True, shell=True)
        print(f"System date changed to {new_date}.")
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to change the date. Error: {e}")

def get_date_range(start_date, end_date):
    """Generates a list of dates between start_date and end_date inclusive."""
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date)
        current_date += timedelta(days=1)
    return date_list

def create_folder(folder_name):
    """Creates a folder with the specified name."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def create_file(folder_name, file_name):
    """Creates a file inside the specified folder."""
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as file:
        file.write("Date, Iteration\n")  
    return file_path

def write_to_file(file_path, content):
    """Appends content to the specified file."""
    with open(file_path, 'a') as file:
        file.write(content + "\n")

def main():
    # Note: 
    print("**Note: Please disconnect the device from internet before starting the script")
    print("**Note: Please run this script in terminal having admin priviledges ")
    print("**Note: Please ensure that your current selected date formate should DD-MM-YYYY")


    # Get user inputs
    start_date_input = input("Enter the starting date (DD-MM-YYYY): ")
    end_date_input = input("Enter the ending date (DD-MM-YYYY): ")
    file_name = input("Enter the name and type of file (e.g., data.txt): ")
    folder_name = input("Enter the name of the folder: ")

    # Parse dates with proper error handling
    try:
        start_date = datetime.strptime(start_date_input, "%d-%m-%Y")
        end_date = datetime.strptime(end_date_input, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return

    if start_date > end_date:
        print("Starting date cannot be after ending date.")
        return

    # Create folder and file
    create_folder(folder_name)
    create_file(folder_name, file_name)

    # Changing the current working directory to the newly created folder
    os.chdir(folder_name)

    # Run git commands
    os.system("git init")  # Initialize a git repository

    # Define random commit messages
    commit_messages = [
        "Updated data entries",
        "Fixed a bug in the callback function",
        "Optimized operations",
        "Added new functionality",
        "Refactored code structure",
        "Improved file handling",
        "Enhanced date processing",
        "Performed maintenance",
        "Resolved minor issues",
        "Added iteration data",
        "Removed Dead Code",
        "Added comments for improved readability",
        "Added annotations",
        "Changed working directory",
        "Updated paths"
    ]

    # Loop through dates and perform operations
    date_range = get_date_range(start_date, end_date)

    # Randomly decide whether to skip the iteration
    skip_iteration_probability = 0.20  # 20% chance

    initial_commit = True

    for date in date_range:
        if random.random() < skip_iteration_probability:
            print(f"Skipping iteration for date {date.strftime('%d-%m-%Y')}")
            continue  # Skipping the current iteration

        # Changing the system date
        change_system_date(date.strftime('%d-%m-%Y'))

        random_value = random.randint(1, 12)
        for i in range(1, random_value + 1):
            # Performing operations 
            operation_result = f"Date: {date.strftime('%d-%m-%Y')}, Iteration: {i}"
            print(operation_result)
            write_to_file(file_name, operation_result)
            commit_message = random.choice(commit_messages)
            os.system("git add .")  
            # Added functionality for initial commit
            if(initial_commit):
                os.system("git commit -m \"Initial Commit\"") 
                initial_commit = False
            else:
                os.system(f"git commit -m \"{commit_message}\"") 

    print("Operations performed successfully.")

if __name__ == "__main__":
    main()
