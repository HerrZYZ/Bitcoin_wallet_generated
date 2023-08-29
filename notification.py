```python
from datetime import datetime
from user import User

class Notification:
    def __init__(self, user: User, message: str):
        self.user = user
        self.message = message
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Notification for {self.user.username} at {self.timestamp}: {self.message}"
```
