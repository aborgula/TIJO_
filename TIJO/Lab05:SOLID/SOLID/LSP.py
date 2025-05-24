# Naruszona zasada LSP

from abc import ABC, abstractmethod

class IBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class StandardAccount(IBankAccount):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if self._balance - amount >= 100: # Minimum balance must be 100
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")

class SavingsAccount(IBankAccount):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if self._balance - amount >= 100: # Minimum balance must be 100
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")











----------------------------------------------
class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")

    def get_balance(self):
        return self._balance


class SavingsAccount:

    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if self._balance - amount >= 100: # Minimum balance must be 100
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")


def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")

def perform_transaction(account: SavingsAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    account.withdraw(withdraw_amount)
    print(f"Balance after transaction: {account.get_balance()}")

# Usage
regular_account = BankAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Works
perform_transaction(savings_account, 500, 350)  # Exception!

----------------------
chat



from abc import ABC, abstractmethod


class IBankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class StandardAccount(IBankAccount):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception("Insufficient funds")

    def get_balance(self):
        return self._balance


class SavingsAccount(IBankAccount):
    def __init__(self):
        self._balance = 0
        self._minimum_balance = 100

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount >= self._minimum_balance:
            self._balance -= amount
        else:
            raise Exception("Minimum balance for savings account is 100")

    def get_balance(self):
        return self._balance


def perform_transaction(account: IBankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    try:
        account.withdraw(withdraw_amount)
        print(f"Balance after transaction: {account.get_balance()}")
    except Exception as e:
        print(f"Transaction failed: {e}")


# Usage
regular_account = StandardAccount()
savings_account = SavingsAccount()

perform_transaction(regular_account, 500, 200)  # Works
perform_transaction(savings_account, 500, 450)  # No exception, but prints an error message
