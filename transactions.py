"""This file initializes data to create transactions."""

import random


# original data in the mempool
transaction1 = {'amount': '30', 'sender': 'Alice', 'receiver': 'Bob'}
transaction2 = {'amount': '200', 'sender': 'Bob', 'receiver': 'Alice'}
transaction3 = {'amount': '300', 'sender': 'Alice', 'receiver': 'Timothy'}
transaction4 = {'amount': '300', 'sender': 'Rodrigo', 'receiver': 'Thomas'}
transaction5 = {'amount': '200', 'sender': 'Timothy', 'receiver': 'Thomas'}
transaction6 = {'amount': '400', 'sender': 'Tiffany', 'receiver': 'Xavier'}


mempool = [
    transaction1,
    transaction2,
    transaction3,
    transaction4,
    transaction5,
    transaction6,
]

# add a transaction to the mempool
my_transaction = dict(amount='123', sender='Gerald', receiver='Rob')
mempool.append(my_transaction)
