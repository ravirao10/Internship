# Parent Class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: ₹{self.balance}")


# Child Class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance}")


# Child Class
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.account_holder} withdrew ₹{amount} with overdraft. New Balance: ₹{self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit!")



# Create SavingsAccount object
savings = SavingsAccount("ALICE", 10000, 0.08)
savings.display_balance()
savings.deposit(2000)
savings.withdraw(3000)
savings.add_interest()
savings.display_balance()

print("\n--- Current Account ---")
# Create CurrentAccount object
current = CurrentAccount("BOB", 5000, 10000)
current.display_balance()
current.deposit(4000)
current.withdraw(2000)
current.withdraw_with_overdraft(12000)  
current.withdraw_with_overdraft(20000)  
current.display_balance()
