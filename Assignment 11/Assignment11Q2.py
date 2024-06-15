import os
import sys
import hashlib
def find_duplicate_files(directory):
    try:
        files = {}
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                file_hash = hashfile(path)
                if file_hash in files:
                    files[file_hash].append(filename)
                else:
                    files[file_hash] = [filename]

        duplicates = {k: v for k, v in files.items() if len(v) > 1}
        return duplicates
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def hashfile(path, blocksize=65536):
    """Calculate the hash of a file."""
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        buf = f.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(blocksize)
    return hasher.hexdigest()

def write_to_log(duplicates):
    try:
        with open("Log.txt", "w") as logfile:
            for hashvalue, filenames in duplicates.items():
                logfile.write(f"Hash: {hashvalue}\n")
                logfile.write("Files:\n")
                for filename in filenames:
                    logfile.write(f"    {filename}\n")
                logfile.write("\n")
        print("Duplicate files logged in 'Log.txt'.")
    except Exception as e:
        print(f"An error occurred while writing to log file: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicate.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    duplicates = find_duplicate_files(directory)
    if duplicates:
        write_to_log(duplicates)
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()