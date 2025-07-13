# Henry Huitema
# This program creates and tests a BankAcct class containing a name, account number, balance, and interest.
# The BankAcct class has methods for adjusting interest, withdrawing, depositing, and displaying balance.
# The class also has a method for calculating flat interest based on a given number of days.

class BankAcct:
    def __init__(self, name, acct_number, balance, interest):
        self.name = name
        self.acct_number = acct_number
        self.balance = balance
        self.interest = interest

    def __str__(self):
        return f"Balance: ${self.balance}\nInterest rate: {self.interest*100}%"

    def setInterest(self, interest):
        self.interest = interest

    def deposit(self, deposit):
        self.balance = self.balance + deposit

    def withdraw(self, withdraw):
        self.balance = self.balance - withdraw

    def showBalance(self):
        print(f"Balance: ${self.balance}")

    def calculateInterest(self, days):
        # Flat interest, by day
        interestGain = self.balance * self.interest * days
        print(f"${round(interestGain, 2)}")
        
def test():
    # __init__
    testAccount = BankAcct("Example Name", 111111, 5000, 0.05)
    # Deposit/Show Balance
    testAccount.showBalance()
    testAccount.deposit(550)
    # Withdraw
    testAccount.showBalance()
    testAccount.withdraw(375)
    # __str__
    print(testAccount)
    # Set Interest
    testAccount.setInterest(0.08)
    print(testAccount)
    # Calculate Interest
    testAccount.calculateInterest(4)

def main():
    test()

if __name__ == "__main__":
    main()
