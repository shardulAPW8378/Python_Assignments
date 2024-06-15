import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            if f1.read() == f2.read():
                print("Success: Files have the same contents.")
            else:
                print("Failure: Files have different contents.")
    except FileNotFoundError:
        print("One or both files not found.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_files(file1, file2)

if __name__ == "__main__":
    main()