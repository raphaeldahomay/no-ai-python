Objective
Create a class called BankAccount that simulates a simple banking system.

Each bank account should have its own information and allow certain operations.

1. Initialize a bank account
When creating an account, the user must provide:
- owner — name of the account holder.
- balance — initial balance, which should default to 0 if not provided.
- account_id — a unique identifier automatically generated for each account, starting at 1.

2. Implement four methods
Method	Expected behavior
deposit(amount)	Adds money to the balance. Rejects amounts ≤ 0.
withdraw(amount)	Removes money. Rejects amounts ≤ 0 or greater than the balance.
transfer(other_account, amount)	Transfers money from the current account to another account, provided the amount is valid.
get_info()	Returns a dictionary containing account_id, owner, and balance.

For invalid operations, you can return False. Successful operations should return True.