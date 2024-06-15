def minn():
    n = int(input("Number of elements: "))
    elements = list(map(int, input("Input Elements: ").split()))
    return min(elements)

def main():
   
    print("Output:", minn())

if __name__ == "__main__":
    main()