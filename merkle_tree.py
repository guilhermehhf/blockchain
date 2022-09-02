import hashlib
import math
import random


class Node:
    def __init__(self, hash_left, hash_right):
        self.parent = None
        self.hash_left = hash_left
        self.hash_right = hash_right
        self.hash = self.node_hash() 

    def node_hash(self):
        hash = self.hash_left + self.hash_right
        return hashlib.sha256(hash.encode('utf8')).hexdigest()

    def __str__(self):
        return f'Node\n hash_left: {self.hash_left}\n hash_right: {self.hash_right}\n hash: {self.hash}'

class MerkleTree:
    def __init__(self, transactions):
        self.tree = []
        self.transactions = transactions
        self.nodes = []
        self.add_ficticional_transactions()
        self.transactions_to_nodes()
        self.fill_tree()

    def log2(self, x):
        if x == 0:
            return False
        return (math.log10(x) / math.log10(2))

    def is_power_of_two(self, n):
        return (math.ceil(self.log2(n)) == math.floor(self.log2(n)))

    def transactions_to_nodes(self):
        for i in range(0,len(self.transactions),2):
            hash1 = hashlib.sha256(self.transactions[i].encode('utf8')).hexdigest()
            hash2 = hashlib.sha256(self.transactions[i+1].encode('utf8')).hexdigest()
            node = Node(hash1, hash2)
            self.tree.append(node)

    def fill_tree(self):
        nodes = self.tree.copy()
        root = None
        while len(nodes) > 1:
            node1 = nodes.shift().hash
            node2 = nodes.shift().hash
            aux = Node(node1, node2)
            self.tree.append(aux)


        list_of_nodes = self.transactions
        while not list_of_nodes:
            aux = list_of_nodes.shift()


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