def count_string_frequency(filename, search_string):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            frequency = contents.count(search_string)
            return frequency
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def main():
    filename = input("Enter file name: ")
    search_string = input("Enter string to search: ")
    frequency = count_string_frequency(filename, search_string)
    if frequency is not None:
        print(f"Frequency of '{search_string}' in '{filename}': {frequency}")

if __name__ == "__main__":
    main()