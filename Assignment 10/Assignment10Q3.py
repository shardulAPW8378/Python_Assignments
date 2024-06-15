import os
import sys

def copy_files(src_dir, dest_dir):
    try:
        os.mkdir(dest_dir)
        files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
        for file in files:
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(dest_dir, file)
            with open(src_file, 'rb') as fsrc, open(dest_file, 'wb') as fdest:
                fdest.write(fsrc.read())
        print(f"All files copied from '{src_dir}' to '{dest_dir}'.")
    except FileNotFoundError:
        print(f"Directory '{src_dir}' not found.")
    except FileExistsError:
        print(f"Directory '{dest_dir}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryCopy.py <source_directory> <destination_directory>")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()