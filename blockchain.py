"""This file contains the class for the Blockchain."""

from block import Block


class Blockchain:
    """docstring for Blockchain"""
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        """First block of the Blockchain"""

        transactions = {}
        genesis_block = Block(transactions, '0')
        self.chain.append(genesis_block)

    def print_blocks(self):
        """Print contents of blockchain."""

        for i, current_block in enumerate(self.chain):
            print('=====')
            print(f'Block {i} {current_block}')
            current_block.print_block()
            print('=====')
            print()

    def add_block(self, transactions):
        """Add a block to the blockchain's chain."""

        previous_block_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_block_hash)
        proof = self.proof_of_work(new_block)
        new_block.proof = proof
        self.chain.append(new_block)

        return new_block

    def validate_chain(self):
        """Check to see if blocks are linked to each other properly."""

        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.generate_hash():
                print('WARNING!! The current hash of the block does not equal '
                      'the generated hash of the block!!!')

                return False

            if current.previous_hash != previous.generate_hash():
                print('WARNING!! The previous hash of the block does not equal'
                      ' the generated hash of the previous block!!!')

                return False

        print('Blockchain is valid!')

        return True

    def proof_of_work(self, block, difficulty=2):
        """Implement a proof of work in the blockchain."""

        proof = block.hash

        while not proof.startswith('0' * difficulty):
            block.nonce += 1
            proof = block.generate_hash()

        block.nonce = 0

        return proof
