def Sum_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    num = int(input("Enter a number: "))
    result = Sum_digits(num)
    print("Sum of digits in", num, "is:", result)

if __name__ == "__main__":
    main()