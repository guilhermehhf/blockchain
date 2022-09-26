from transaction import Transaction

users = {
    1: 'Hank',
    2: 'Walter',
    3: 'Marie',
    4: 'Skyler',
},
transactions = [
    Transaction(users.get(1), users.get(2), 30),
    Transaction(users.get(2), users.get(1), 7),
    Transaction(users.get(1), users.get(3), 10),
    Transaction(users.get(4), users.get(2), 5),
    Transaction(users.get(2), users.get(3), 4),
    Transaction(users.get(4), users.get(2), 2),
    Transaction(users.get(3), users.get(1), 10),
    Transaction(users.get(3), users.get(4), 15),
]