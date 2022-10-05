from block import Block
from datetime import datetime
from transaction import Transaction

class BlockChain():
    def __init__(self):
        self.blocks = [self.__add_block_genesis()]
        

    def __add_block_genesis(self):
        timestamp = datetime.now().timestamp()
        users = [
            'Hank',
            'Walter',
            'Marie',
            'Skyler',
            'Jesse',
            'Gus',
            'Flynn',
            'Jane'
        ]
        transactions = []
        for user in users:
            transactions.append(Transaction('Genesis', user, 1000))

        return Block(0,transactions,timestamp,0)

    def add_block(self, transactions):
        index = len(self.blocks)
        timestamp = datetime.now().timestamp()
        previous_hash = self.blocks[-1].get_hash()
        [is_possible, message] = self.is_possible_add_block_with_current_transactions(transactions)
        if is_possible:
            self.blocks.append(Block(index,transactions,timestamp,previous_hash))
            return message
        else:
            return message

    def is_possible_add_block_with_current_transactions(self, transactions):
        for i in range(len(transactions)-1, -1, -1):
            sum = -abs(transactions[i].message)
            sender = transactions[i].sender
            sum = self.is_positive_balance(sum,sender,transactions[:i])

            if(sum < 0):
                for block in self.blocks:
                    sum = self.is_positive_balance(sum,sender,block.transactions)
                    if sum >= 0:
                        break
                
                if sum < 0:
                    return {False,f'A transação de {transactions[i].sender} para {transactions[i].to} de {transactions[i].message} não pode ser feita'}

        return { True,'Bloco adicionado'}

    def is_positive_balance(self, sum, sender, transactions):
        for j in range(len(transactions) - 1, -1, -1):
            sum = self.sub_or_add(sum, sender, transactions[j])
            if sum >= 0:
                return sum
        return sum

    def sub_or_add(self, sum, sender, transaction):
        if sender == transaction.sender:
            return sum - transaction.message
        elif sender == transaction.to:
            return sum + transaction.message
        return sum

    def print_blocks(self):
        for i in range(len(self.blocks)):
            print(self.blocks[i])