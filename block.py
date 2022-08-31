
#create a class named Bloco with parameters index, transactions, timestamp, previous_hash, nonce
import hashlib

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = self.validHash()
        self.hash = self.get_hash()

    def validHash(self):
        nonce = 1
        while(True):
            string = f'{self.index} {self.transactions} {self.timestamp} {self.previous_hash} {nonce}'
            hash = hashlib.sha256(string.encode()).hexdigest()
            if(hash.startswith("000")):
                break
            nonce += 1
        return nonce

    def get_hash(self):
        string = f'{self.index} {self.transactions} {self.timestamp} {self.previous_hash} {self.nonce}'
        return hashlib.sha256(string.encode()).hexdigest()

    def __str__(self):
        return f'Block(\n   index: {self.index},\n   transactions: {self.transactions},\n   timestamp: {self.timestamp},\n   previous_hash:  {self.previous_hash},\n   nonce: {self.nonce}, \n   hash: {self.get_hash()}\n)'