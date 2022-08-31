from audioop import add
from blockchain import BlockChain

blockchain = BlockChain('block genesis')

def add_blocks(quantity_of_blocks):
    for i in range(quantity_of_blocks-1):
        blockchain.add_block(f'block {len(blockchain.blocks)}')

add_blocks(10)
blockchain.print_blocks()