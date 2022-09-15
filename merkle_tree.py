import hashlib
import math
import random


class Node:
    def __init__(self, **kwargs):
        self.daddy = None
        self.node_left = kwargs.get('node_left')
        self.node_right = kwargs.get('node_right')
        if(self.node_left != None and self.node_right != None):
            self.node_left.daddy = self
            self.node_right.daddy = self
            self.hash = self.node_hash()
        else:
            self.hash = hashlib.sha256(kwargs.get('transaction').encode('utf8')).hexdigest()

    def node_hash(self):
        hash = f'{self.node_left.hash} + {self.node_right.hash}'
        return hashlib.sha256(hash.encode('utf8')).hexdigest()

    def __str__(self):
        if(self.node_left != None and self.node_right != None):
            return f'Node\n node_left: {self.node_left.hash}\n node_right: {self.node_right.hash}\n self.hash: {self.hash}'
        else:
            return f'Leaf: hash = {self.hash}'

class MerkleTree:
    def __init__(self, transactions):
        self.tree = []
        self.transactions = transactions
        self.nodes = []
        self.add_ficticional_transactions()
        self.transactions_to_nodes()
        self.root = self.tree[-1]

    def log2(self, x):
        if x == 0:
            return False
        return (math.log10(x) / math.log10(2))

    def is_power_of_two(self, n):
        return (math.ceil(self.log2(n)) == math.floor(self.log2(n)))

    def transactions_to_nodes(self):
        aux = []
        for transaction in self.transactions:
            node = Node(transaction = transaction)
            aux.append(node)
            self.tree.append(node)

        
        while len(aux) > 1:
            node_left = aux.pop(0)
            node_right = aux.pop(0)
            node = Node(node_left = node_left, node_right = node_right)
            aux.append(node)
            self.tree.append(node)


    def add_ficticional_transactions(self):
        transactions_length = len(self.transactions)
        if not self.is_power_of_two(transactions_length):
            n = 1
            while True:
                power = int(math.pow(2,n))
                if transactions_length  < power:
                    len_need_to_be_added = power - transactions_length
                    # print(len_need_to_be_added)
                    num_need_to_be_added = random.sample(range(0,transactions_length-1) , len_need_to_be_added)
                    for num in num_need_to_be_added:
                        self.transactions.append(self.transactions[num])
                    break
                n = n + 1