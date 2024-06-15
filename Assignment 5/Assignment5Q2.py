def pattern(n):
    if n > 0:
        pattern(n - 1)
        print(n , end=" ")
        

def main():
    num = int(input("Enter a number: "))
    pattern(num)

if __name__ == "__main__":
    main()