class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value * 2

    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        return sum(self.Factors()) - self.Value

def main():
    
    num1 = Numbers(int(input("Enter a number: ")))
    num2 = Numbers(int(input("Enter another number: ")))

    
    print("Is num1 prime?", num1.ChkPrime())
    print("Is num1 perfect?", num1.ChkPerfect())
    print("Factors of num1:", num1.Factors())
    print("Sum of factors of num1:", num1.SumFactors())

    
    print("Is num2 prime?", num2.ChkPrime())
    print("Is num2 perfect?", num2.ChkPerfect())
    print("Factors of num2:", num2.Factors())
    print("Sum of factors of num2:", num2.SumFactors())

if __name__ == "__main__":
    main()