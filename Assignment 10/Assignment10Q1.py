import os
import sys

def search_files(directory, extension):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        return files
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryFileSearch.py <directory> <extension>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]

    files = search_files(directory, extension)

    if files:
        print(f"Files with extension '{extension}' in directory '{directory}':")
        for file in files:
            print(file)
    else:
        print(f"No files with extension '{extension}' found in directory '{directory}'.")

if __name__ == "__main__":
    main()