## Code: user.py
```python
import bcrypt
from wallet import Wallet

class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email
        self.wallet = None

    def hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def create_wallet(self) -> Wallet:
        if self.wallet is None:
            self.wallet = Wallet()
        return self.wallet
```
