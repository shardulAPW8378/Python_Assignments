import Arithmatic

def main():
    num1 = int(input("Enter The Number :"))
    num2 = int(input("Enter The Number :"))
    print("Addition Is :",Arithmatic.Add(num1,num2))
    print("Subtraction Is :",Arithmatic.Sub(num1,num2))
    print("Multiplication Is :",Arithmatic.Mult(num1,num2))
    print("Division Is :",Arithmatic.Div(num1,num2))
if __name__ =="__main__":
    main()