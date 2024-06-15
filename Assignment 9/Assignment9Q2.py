def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    filename = input("Enter file name: ")
    display_file_contents(filename)

if __name__ == "__main__":
    main()