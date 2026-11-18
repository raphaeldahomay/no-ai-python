## raw findings, written 26min31
def register_transac(func):
    def wrapper():
        type = func
        amount = func(**args)
        func()
        result = func()
        return result
    return wrapper


class BankAccount:
    _account_number = 0
    number_accounts = 0

    def __init__(self, owner, balance = 0):
        self._owner = owner
        self._account_number += 1
        self._balance = balance
        number_accounts += 1

    @balance.setter
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self._balance += amount
        return True

    @balance.setter
    def withdraw(self, amount):
        if amount < 0 or amount > self._balance:
            raise ValueError("Amount cannot be negative or superior to balance")

        self._balance -= amount
        return True

    @classmethod
    def from_dict(cls, data):
        return cls(data['owner'], data['balance'])

    @classmethod
    def get_total_accounts(cls):
        return cls.number_accounts


class StandardAccount(BankAccount):
    def __init__(self, owner, balance = 0):
        super().__init__(self, owner, balance)
        self._type = 'standard'


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance = 0):
        super().__init__(self, owner, balance)
        self._type = 'savings'

    @property
    def get_balance(self):
        return self.balance * 1.02



## solution ##

import time
from functools import wraps

def register_transac(func):
    @wraps(func)
    def wrapper(self, amount):
        start = time.perf_counter()
        success = False

        try:
            result = func(self, amount)
            success = True
            return result

        finally:
            duration = time.perf_counter() - start

            self._history.append({
                "type": func.__name__,
                "amount": amount,
                "success": success,
                "duration_seconds": duration
            })

    return wrapper


class BankAccount:
    number_accounts = 0

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        BankAccount.number_accounts += 1

        self._owner = owner
        self._account_number = f"ACC{BankAccount.number_accounts:03d}"
        self._balance = balance
        self._history = []

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def history(self):
        return [entry.copy() for entry in self._history]

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @register_transac
    def deposit(self, amount):
        if not self.validate_amount(amount):
            raise ValueError("Amount must be positive")

        self._balance += amount
        return True

    @register_transac
    def withdraw(self, amount):
        if not self.validate_amount(amount):
            raise ValueError("Amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        return True

    @classmethod
    def from_dict(cls, data):
        return cls(data["owner"], data.get("balance", 0))

    @classmethod
    def get_total_accounts(cls):
        return BankAccount.number_accounts


class StandardAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self._type = "standard"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)

        if not 0 <= interest_rate <= 1:
            raise ValueError("Invalid interest rate")

        self._type = "savings"
        self._interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        return interest


# Testing

account = StandardAccount("John", 1500)

account.deposit(500)
account.withdraw(300)

print(account.balance)  # 1700

try:
    account.withdraw(5000)
except ValueError as error:
    print(error)  # Insufficient funds

print(account.history)
# [
#   {'type': 'deposit', 'amount': 500, 'success': True},
#   {'type': 'withdraw', 'amount': 300, 'success': True},
#   {'type': 'withdraw', 'amount': 5000, 'success': False}
# ]

savings = SavingsAccount("Alice", 2000, 0.05)

savings.apply_interest()

print(savings.balance)  # 2100.0

print(BankAccount.get_total_accounts())  # 2

customer_data = {
    "owner": "Michael",
    "balance": 1000
}

new_account = StandardAccount.from_dict(customer_data)

print(new_account.balance)  # 1000
print(BankAccount.get_total_accounts())  # 3
