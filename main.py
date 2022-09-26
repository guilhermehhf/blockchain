from blockchain import BlockChain
from merkle_tree import MerkleTree
blockchain = BlockChain('block genesis')
from fulfilling_transactions import transactions



def add_blocks(quantity_of_blocks):
    for i in range(quantity_of_blocks-1):
        blockchain.add_block(f'block {len(blockchain.blocks)}')

add_blocks(10)
blockchain.print_blocks()

# mt = MerkleTree(['mt','mt2','mt3','mt4','mt5','mt6','mt7','mt8'])


# print(mt.transactions)
# print(len(mt.tree))
# # print(mt.tree[14])
# aux = []
# aux.append(mt.tree[8])
# while aux:
#     node = aux.pop(0)
#     if node.daddy != None:
#         aux.append(node.daddy)
#     print(node)