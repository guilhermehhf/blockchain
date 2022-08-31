from block import Block
from datetime import datetime

class BlockChain():
    def __init__(self, transactions):
        self.blocks = [self.__add_block_genesis(transactions)]

    def __add_block_genesis(self, transactions):
        timestamp = datetime.now().timestamp()
        return Block(0,transactions,timestamp,0)

    def add_block(self, transactions):
        index = len(self.blocks)
        timestamp = datetime.now().timestamp()
        previous_hash = self.blocks[-1].get_hash()
        self.blocks.append(Block(index,transactions,timestamp,previous_hash))

    def print_blocks(self):
        for i in range(len(self.blocks)):
            print(self.blocks[i])