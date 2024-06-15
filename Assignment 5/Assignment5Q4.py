def SumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + SumDigits(n // 10)

def main():
    num = int(input("Enter a number: "))
    print("Output:", SumDigits(num))

if __name__ == "__main__":
    main()