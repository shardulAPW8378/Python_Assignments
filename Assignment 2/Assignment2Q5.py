def PrimeNum(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    num = int(input("Enter a number: "))
    if PrimeNum(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

if __name__ == "__main__":
    main()