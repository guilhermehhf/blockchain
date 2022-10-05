from transaction import Transaction
from random import randint

users:dict = {
    1: 'Hank',
    2: 'Walter',
    3: 'Marie',
    4: 'Skyler',
}

def random_two_users():
    user1 = randint(1, len(users))
    user2 = randint(1, len(users))
    while user1 == user2:
        user2 = randint(1, len(users))

    return user1, user2

def random_message():
    return randint(1,5)

def random_transactions():
    transactions_return = []
    for i in range(8):
        user1, user2 = random_two_users()
        transactions_return.append(Transaction(users.get(user1), users.get(user2), random_message()))
    return transactions_return