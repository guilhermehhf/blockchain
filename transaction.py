class Transaction():
    def __init__(self, sender, to, message):
        self.sender = sender
        self.to = to
        self.message = message
    def __str__(self):
        return f'{self.sender}->{self.to}:{self.message}'