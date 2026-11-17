## raw findings, written in 13min40
class BankAccount:
    def __init__(self, owner, balance, account_id):
        self.owner = owner
        self.balance = balance if not None else 0
        self.account_id = account_id

    def deposit(self, amount):
        self.balance += amount if amount >= 0 else print("Please enter a positive amount.")

    def withdraw(self, amount):
        self.balance -= amount if amount <= self.balance and amount >= 0 else print("Please withdraw a valid amount.")

    def transfer(self, other_account_id, amount):
        self.balance += amount if self.account_id == other_account_id else print("This account_id is not valid.")

    def get_info(self):
        print(f" owner: {self.owner}, balance: {self.balance}, account_id: {self.account_id}")


## corected version
class BankAccountRefined:
    next_id = 1

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_id = BankAccountRefined.next_id
        BankAccountRefined.next_id += 1

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        return True

    def transfer(self, other_account, amount):
        if self is other_account:
            return False

        if amount <= 0 or amount > self.balance:
            return False

        self.balance -= amount
        other_account.balance += amount
        return True

    def get_info(self):
        return {
            "account_id": self.account_id,
            "owner": self.owner,
            "balance": self.balance
        }


## testing
account_1 = BankAccountRefined("Raphael", 1000)
account_2 = BankAccountRefined("John", 500)

account_1.deposit(200)
account_1.withdraw(100)
account_1.transfer(account_2, 300)

print(account_1.get_info())
print(account_2.get_info())

# result
{'account_id': 1, 'owner': 'Raphael', 'balance': 800}
{'account_id': 2, 'owner': 'John', 'balance': 800}