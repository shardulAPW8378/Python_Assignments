from functools import reduce

def filter_numbers(numbers):
    return list(filter(lambda x: x >= 70 and x <= 90, numbers))

def increase_by_10(numbers):
    return list(map(lambda x: x + 10, numbers))

def multiply_numbers(numbers):
    return reduce(lambda x, y: x * y, numbers)

def main():
    
    input_list = list(map(int, input("Enter a list of numbers : ").split()))

    
    filtered_list = filter_numbers(input_list)
    print("List after filter:", filtered_list)

    
    mapped_list = increase_by_10(filtered_list)
    print("List after map:", mapped_list)

    
    result = multiply_numbers(mapped_list)
    print("Output of reduce:", result)

if __name__ == "__main__":
    main()