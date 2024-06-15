def display(n):
    for i in range(n):
        print("  *  " * n )
            


def main():
    num = int(input("Enter the number:"))
    display(num)

if __name__ =="__main__":
    main()