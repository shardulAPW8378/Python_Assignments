from functools import reduce

def Checkprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def Double(n):
    return n * 2


input_list = list(map(int, input("Enter a list of numbers : ").split()))


filtered_list = list(filter(Checkprime, input_list))
print("After filter:", filtered_list)


mapped_list = list(map(Double, filtered_list))
print("After map:", mapped_list)


result = reduce(lambda x, y: x if x > y else y, mapped_list)
print("Output of reduce:", result)