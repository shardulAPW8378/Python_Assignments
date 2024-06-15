import sys
import psutil

def get_process_info(process_name):
    for process in psutil.process_iter(['pid', 'name', 'username']):
        if process.info.get('name', '') == process_name:
            return {
                'Name': process.info.get('name', ''),
                'PID': process.info['pid'],
                'Username': process.info['username']
            }
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <process_name>")
        sys.exit(1)
    
    process_name = sys.argv[1]
    process_info = get_process_info(process_name)
    if process_info:
        print(f"Name: {process_info['Name']}, PID: {process_info['PID']}, Username: {process_info['Username']}")
    else:
        print(f"Process '{process_name}' is not running.")

if __name__ == "__main__":
    main()
