import sys

def copy_file_contents(src_filename, dest_filename):
    try:
        with open(src_filename, 'r') as src_file:
            with open(dest_filename, 'w') as dest_file:
                dest_file.write(src_file.read())
        print(f"Contents copied from '{src_filename}' to '{dest_filename}'.")
    except FileNotFoundError:
        print(f"File '{src_filename}' not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_filename>")
        sys.exit(1)

    src_filename = sys.argv[1]
    dest_filename = "Demo.txt"
    copy_file_contents(src_filename, dest_filename)

if __name__ == "__main__":
    main()