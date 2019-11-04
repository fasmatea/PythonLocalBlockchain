"""This module initializes data to create a mempool containing random
transactions. It is only used for the example script, since in a real scenario
we will be populating the blockchain with actual values.
"""

from random import randint, choice


def create_mempool(nb_transactions):
    """Create a mempool containing nb_transactions."""

    return [create_transaction() for i in range(nb_transactions)]


def create_name(min_letters, max_letters):
    """Create a random name with a number of letters that range in between
    min_letters and max_letters.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([
        choice(alphabet)
        for i in range(randint(min_letters, max_letters))
    ])


def create_transaction():
    """Create one transaction from random values."""

    return dict(
        sender=create_name(3, 10),
        receiver=create_name(3, 10),
        amount=randint(0, 1000),
    )
