import os
import sys

def copy_files(src_dir, dest_dir, ext):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        files = [f for f in os.listdir(src_dir) if f.endswith(ext) and os.path.isfile(os.path.join(src_dir, f))]
        for file in files:
            src_file = os.path.join(src_dir, file)
            dest_file = os.path.join(dest_dir, file)
            with open(src_file, 'rb') as fsrc, open(dest_file, 'wb') as fdest:
                fdest.write(fsrc.read())
        print(f"All files with extension '{ext}' copied from '{src_dir}' to '{dest_dir}'.")
    except FileNotFoundError:
        print(f"Directory '{src_dir}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python DirectoryCopyExt.py <source_directory> <destination_directory> <extension>")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    ext = sys.argv[3]

    copy_files(src_dir, dest_dir, ext)

if __name__ == "__main__":
    main()