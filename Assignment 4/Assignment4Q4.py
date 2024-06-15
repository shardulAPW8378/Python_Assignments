from functools import reduce

def filterEven(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def squareNumbers(numbers):
    return list(map(lambda x: x ** 2, numbers))

def sumNumbers(numbers):
    return reduce(lambda x, y: x + y, numbers)

def main():
    
    input_list = list(map(int, input("Enter a list of numbers : ").split()))

    
    filtered_list = filterEven(input_list)
    print("List after filter:", filtered_list)

    
    mapped_list = squareNumbers(filtered_list)
    print("List after map:", mapped_list)

    
    result = sumNumbers(mapped_list)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()