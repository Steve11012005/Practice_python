class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"#{amount} deposited. New balance: #{self.balance}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"#{amount} withdrawn. Remaining balance: #{self.balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return f"Current balance: #{self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=3.5):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Interest applied: #{interest}. New balance: #{self.balance}"
    # Override the withdraw method to add restrictions

    def withdraw(self, amount):
        # Limit withdrawals to 50,000 Naira per transaction for savings accounts
        if amount > 50000:
            return "Withdrawal limit exceeded. Maximum withdrawal per transaction is #50000"
        return super().withdraw(amount)


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=20000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    # Override the withdraw method to allow overdrafts

    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            return f"#{amount} withdrawn. Remainng balance: #{self.balance}"
        return "Amount exceeds available balance and overdraft limit"


# Create accounts
savings = SavingsAccount("0123456789", "Adaobi Eze", 100000)
current = CurrentAccount("9876543210", "Chinedu Obi", 50000)

# Use methods
print(savings.deposit(50000))
print(savings.withdraw(60000))
print(savings.withdraw(40000))
print(savings.apply_interest())

print(current.deposit(30000))
print(current.withdraw(70000))
print(current.get_balance())
