from block import Block
from datetime import datetime

class BlockChain():
    def __init__(self, transactions):
        self.users = {
            1: 'Hank',
            2: 'Walter',
            3: 'Marie',
            4: 'Skyler',
            5: 'Jessie',
            6: 'Gus',
            7: 'Flynn'
        }
        self.blocks = [self.__add_block_genesis(transactions)]
        

    def __add_block_genesis(self, transactions):
        timestamp = datetime.now().timestamp()
        return Block(0,transactions,timestamp,0)

    def add_block(self, transactions):
        index = len(self.blocks)
        timestamp = datetime.now().timestamp()
        previous_hash = self.blocks[-1].get_hash()
        is_possible, message = self.is_possible_add_with_current_transactions(transactions)
        if is_possible:
            self.blocks.append(Block(index,transactions,timestamp,previous_hash))
            return message
        else:
            return message

    def is_possible_add_with_current_transactions(self, transactions):
        for i in range(len(transactions)-1, 0, -1):
            sum = -abs(transactions[i].message)
            sender = transactions[i].sender

            for j in range(i - 1, 0, -1):
                if sender == transactions[j].sender:
                    sum = sum - transactions[j].message
                elif sender == transactions[j].to:
                    sum = sum + transactions[j].message
                
                if sum >= 0:
                    break

            if sum < 0:
                for block in self.blocks:
                    for transaction in block.transactions:
                        if sender == transactions[j].sender:
                            sum = sum - transactions[j].message
                        elif sender == transactions[j].to:
                            sum = sum + transactions[j].message
                        
                        if sum >= 0:
                            break
                return {
                    'bool': False,
                    'message':f'A transação de {transactions[i].sender} para {transactions[i].to} de {transactions[i].message} não pode ser feita'}


            
    def compare_transaction_with_list_of_transactions(self, transaction, transactions_to_compare):
        return None
    def print_blocks(self):
        for i in range(len(self.blocks)):
            print(self.blocks[i])