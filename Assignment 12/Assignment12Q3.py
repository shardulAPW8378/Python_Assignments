import os
import psutil

def get_process_info():
    process_info = []
    for process in psutil.process_iter(['pid', 'name', 'username']):
        process_info.append({
            'Name': process.info['name'],
            'PID': process.info['pid'],
            'Username': process.info['username']
        })
    return process_info

def create_log_file(directory):
    log_file_path = os.path.join(directory, "processes.log")
    with open(log_file_path, "w") as logfile:
        process_info = get_process_info()
        logfile.write("{:<30} {:<10} {:<20}\n".format("Name", "PID", "Username"))
        logfile.write("="*60 + "\n")
        for process in process_info:
            name = process['Name'] if process['Name'] is not None else ''
            pid = process['PID'] if process['PID'] is not None else ''
            username = process['Username'] if process['Username'] is not None else ''
            logfile.write("{:<30} {:<10} {:<20}\n".format(name, pid, username))
    print(f"Process information logged in '{log_file_path}'.")

def main():
    directory = input("Enter the directory name where you want to create the log file: ")
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    elif not os.path.isdir(directory):
        print(f"'{directory}' is not a directory.")
        return

    create_log_file(directory)

if __name__ == "__main__":
    main()
