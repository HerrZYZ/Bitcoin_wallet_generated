```python
## wallet.py
from datetime import datetime
from typing import List
from transaction import Transaction

class Wallet:
    def __init__(self, address: str, balance: float):
        self.address = address
        self.balance = balance
        self.transactions: List[Transaction] = []

    def send_bitcoin(self, amount: float, recipient: str) -> Transaction:
        if self.balance < amount:
            raise Exception("Insufficient balance")
        self.balance -= amount
        transaction = Transaction(self.address, recipient, amount, datetime.now())
        self.transactions.append(transaction)
        return transaction

    def receive_bitcoin(self, amount: float, sender: str) -> Transaction:
        self.balance += amount
        transaction = Transaction(sender, self.address, amount, datetime.now())
        self.transactions.append(transaction)
        return transaction
```
