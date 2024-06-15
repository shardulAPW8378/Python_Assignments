def pattern(n):
    if n > 0:
        print(n , end=" ")
        pattern(n - 1)

def main():
    num = int(input("Enter a number: "))
    pattern(num)

if __name__ == "__main__":
    main()