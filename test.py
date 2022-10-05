from blockchain import BlockChain
from merkle_tree import MerkleTree
from fulfilling_transactions import random_transactions
from transaction import Transaction

blockchain = BlockChain()

def add_blocks(quantity_of_blocks):
    for i in range(quantity_of_blocks-1):
        blockchain.add_block(random_transactions())

add_blocks(10)
blockchain.print_blocks()


# a non existent user try to send "money" to another user
trans = random_transactions()
trans[1] = Transaction('random', 'Walter', 100000000)
message = blockchain.add_block(trans)
print(f'{message}\ntransações no bloco:\n{[str(x) for x in trans]}\n')

# an existent user try to send "money" to another user
trans2 = random_transactions()
trans2[1] = Transaction('Jesse', 'Walter', 100000000)
message = blockchain.add_block(trans2)
print(f'{message}\ntransações no bloco:\n{[str(x) for x in trans2]}')


mt = blockchain.blocks[0].merkle_tree
mt_root = blockchain.blocks[0].merkle_root


print('\nTransações: ',[str(x) for x in mt.transactions])
print('Quantidade de nós na arvore: ',len(mt.tree))

aux = []
aux.append(mt.root)

while aux:
    node = aux.pop(0)
    if node.daddy != None:
        aux.append(node.daddy)
    print(node)