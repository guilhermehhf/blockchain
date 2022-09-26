
#create a class named Bloco with parameters index, transactions, timestamp, previous_hash, nonce
import hashlib

from merkle_tree import MerkleTree

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, difficult):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.merkle_tree = MerkleTree(self.transactions)
        self.merkle_root = self.merkle_tree.root
        self.difficult = difficult
        self.nonce = self.validHash()
        self.hash = self.get_hash()

    def validHash(self):
        nonce = 1
        number_of_zeros = number_of_zeros+"0"*(self.difficult-1)
        while(True):
            string = f'{self.index} {self.transactions} {self.timestamp} {self.previous_hash} {nonce} {self.merkle_root.hash}'
            hash = hashlib.sha256(string.encode()).hexdigest()
            if(hash.startswith(number_of_zeros)):
                break
            nonce += 1
        return nonce

    def get_hash(self):
        string = f'{self.index} {self.transactions} {self.timestamp} {self.previous_hash} {self.nonce} {self.merkle_root.hash}'
        return hashlib.sha256(string.encode()).hexdigest()

    def hash(self, value):
        return hashlib.sha256(value.encode('utf8')).hexdigest()

    def __str__(self):
        return f'Block(\n   index: {self.index},\n   transactions: {self.transactions},\n   timestamp: {self.timestamp},\n   previous_hash:  {self.previous_hash},\n   nonce: {self.nonce}, \n   hash: {self.get_hash()}\n)'