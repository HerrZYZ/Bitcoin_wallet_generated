```python
from datetime import datetime

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Transaction from {self.sender} to {self.recipient} of {self.amount} BTC at {self.timestamp}"
```
