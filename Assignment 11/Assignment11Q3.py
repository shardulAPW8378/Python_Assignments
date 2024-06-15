import os
import sys

def find_duplicate_files(directory):
    try:
        files = {}
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                file_size = os.path.getsize(path)
                if file_size in files:
                    files[file_size].append(filename)
                else:
                    files[file_size] = [filename]

        duplicates = {k: v for k, v in files.items() if len(v) > 1}
        return duplicates
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_duplicate_files(directory, duplicates):
    try:
        log_file = os.path.join(directory, "log1.txt")
        with open(log_file, "w") as logfile:
            for size, filenames in duplicates.items():
                logfile.write(f"Duplicate files with size {size} bytes:\n")
                for filename in filenames[1:]:
                    file_path = os.path.join(directory, filename)
                    os.remove(file_path)
                    logfile.write(f"    Deleted: {filename}\n")
                logfile.write("\n")
        print(f"Duplicate files deleted. Log saved in '{log_file}'.")
    except Exception as e:
        print(f"An error occurred while deleting files: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicateDelete.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    duplicates = find_duplicate_files(directory)
    if duplicates:
        delete_duplicate_files(directory, duplicates)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()