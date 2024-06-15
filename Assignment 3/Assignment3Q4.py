def frequency_of_element():
    n = int(input("Number of elements: "))
    elements = list(map(int, input("Input Elements: ").split()))
    search_element = int(input("Element to search: "))
    return elements.count(search_element)

def main():

    print("Output:", frequency_of_element())

if __name__ == "__main__":
    main()