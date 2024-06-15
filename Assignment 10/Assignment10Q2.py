import os
import sys

def rename_files(directory, ext1, ext2):
    try:
        files = [f for f in os.listdir(directory) if f.endswith(ext1)]
        for file in files:
            old_name = os.path.join(directory, file)
            new_name = os.path.join(directory, file.replace(ext1, ext2))
            os.rename(old_name, new_name)
        print(f"Files with extension '{ext1}' renamed to '{ext2}' in directory '{directory}'.")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python DirectoryRename.py <directory> <old_extension> <new_extension>")
        sys.exit(1)

    directory = sys.argv[1]
    ext1 = sys.argv[2]
    ext2 = sys.argv[3]

    rename_files(directory, ext1, ext2)

if __name__ == "__main__":
    main()