def factorial(n):
    if n< 0 :
        return "Factorial Is Not Defined For Negative Number"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1 , n+1):
            result *= i
        return result 
            


def main():
    num = int(input("Enter the number:"))
    result = factorial(num)
    print("Factorial of " , num , "is:" , result)

if __name__ =="__main__":
    main()