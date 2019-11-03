"""This file contains the class for a Block object"""

from datetime import datetime
from hashlib import sha256


class Block:
    """This is a Block object from the Blockchain"""

    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def print_block(self):
        """Print the block's contents."""
        print(f'timestamp: {self.timestamp}')
        print(f'transactions: {self.transactions}')
        print(f'current hash: {self.hash}')
        print(f'previous hash: {self.previous_hash}')

    def generate_hash(self):
        """Hash the block's contents"""

        block_contents = '{}{}{}{}'.format(
            str(self.timestamp),
            str(self.transactions),
            str(self.nonce),
            str(self.previous_hash),
        )

        block_hash = sha256(block_contents.encode())

        return block_hash.hexdigest()
