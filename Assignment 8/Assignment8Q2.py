class BankAccount:
    ROI = 10.5  

    def __init__(self):
        self.Name = input("Enter account holder's name: ")  
        self.Amount = float(input("Enter initial amount: "))  

    def Display(self):
        print(f"Name: {self.Name.title()}, Amount: {self.Amount:.2f}")

    def Deposit(self):
        deposit_amt = float(input("Enter deposit amount: "))
        self.Amount += deposit_amt

    def Withdraw(self):
        withdraw_amt = float(input("Enter withdrawal amount: "))
        if withdraw_amt <= self.Amount:
            self.Amount -= withdraw_amt
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        self.Amount += interest

def main():
    
    acc1 = BankAccount()
    acc2 = BankAccount()

    
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()
    acc1.Display()

    
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()
    acc2.Display()

if __name__ == "__main__":
    main()