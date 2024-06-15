def sum():
    n = int(input("Number of elements: "))
    elements = list(map(int, input("Input Elements: ").split()))
    return sum(elements)

def main():
    print("Output:", sum())

if __name__ == "__main__":
    main()