import MarvellousNum

def ListPrime():
    n = int(input("Number of elements: "))
    elements = list(map(int, input("Input Elements: ").split()))
    sum_all = sum(elements)
    return sum_all
def main():
    print("Output:", ListPrime())

if __name__ == "__main__":
    main()