import os

def check_file_exists(filename):
    if os.path.exists(filename):
        print(f"File '{filename}' exists in the current directory.")
    else:
        print(f"File '{filename}' does not exist in the current directory.")

def main():
    filename = input("Enter file name: ")
    check_file_exists(filename)

if __name__ == "__main__":
    main()