from blockchain import BlockChain
from fulfilling_transactions import random_transactions
from transaction import Transaction

blockchain = BlockChain()

def add_blocks(quantity_of_blocks):
    for i in range(quantity_of_blocks-1):
        blockchain.add_block(random_transactions())

add_blocks(10)
blockchain.print_blocks()


# a non existent user try to send "money" to another user
transac = random_transactions()
transac[1] = Transaction('random', 'Walter', 100000000)
message = blockchain.add_block(transac)
print(f'{message}\ntransações no bloco:\n{[str(x) for x in transac]}\n')

# an existent user try to send "money" to another user
transac2 = random_transactions()
transac2[1] = Transaction('Jesse', 'Walter', 100000000)
message = blockchain.add_block(transac2)
print(f'{message}\ntransações no bloco:\n{[str(x) for x in transac2]}')