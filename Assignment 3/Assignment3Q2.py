def maxx():
    n = int(input("Number of elements: "))
    elements = list(map(int, input("Input Elements: ").split()))
    return max(elements)

def main():
   
    print("Output:", maxx())

if __name__ == "__main__":
    main()