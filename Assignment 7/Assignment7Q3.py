class Arithmatic:
    def __init__(self, Value1, Value2):  
        self.No1 = Value1  
        self.No2 = Value2  

    def Addition(self):  
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):  
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):  
        Ans = self.No1 * self.No2
        return Ans

    def Division(self):  
        Ans = self.No1 / self.No2
        return Ans

    def Accept(self):
        print("Enter First Number")
        self.No1 = int(input())
        print("Enter Second Number")
        self.No2 = int(input())

def main():
    obj = Arithmatic(0, 0)  
    obj.Accept()  
    Ret = obj.Addition()
    print("Addition Is:", Ret)

    Ret = obj.Subtraction()
    print("Subtraction Is:", Ret)

    Ret = obj.Multiplication()
    print("Multiplication Is:", Ret)

    Ret = obj.Division()
    print("Division Is:", Ret)

if __name__ == "__main__":
    main()
