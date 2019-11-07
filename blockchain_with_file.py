#!/usr/bin/python3

"""This is supposed to be the more definitive version of the Blockchain,
ie. exporting it to a file each time it gets modified.
"""

import os
import json
from blockchain import Blockchain
from block import Block


FILENAME = 'written_blockchain.json'


def main():
    """Search in directory if blockchain file exists. If it doesn't, create the
    file and write a new Blockchain to it.

    Each time a block gets added to the blockchain, update the file, and
    validate its contents.

    The sha256 algorithm will produce the same hash for the same input, so
    creating a new blockchain from scrath with the same blocks (ie. from file)
    should result in the same blockchain.
    """

    if FILENAME not in os.listdir():
        # No blockchain was created, so we create an empty one.
        blockchain = Blockchain()
        print('No blockchain was found, created new blockchain.')

    else:
        blockchain = read_blockchain_from_file(FILENAME)

    if blockchain.validate_chain():
        add_new_transactions_to_blockchain(blockchain)

    else:
        raise AssertionError('The blockchain was tampered with. Quitting.')


def add_new_transactions_to_blockchain(blockchain):
    """Update blockchain with new transactions from input and write the updated
    blockchain to file.
    """

    mempool = []
    nb_of_new_transactions = None
    while not nb_of_new_transactions:
        try:
            nb_of_new_transactions = int(input(
                "How many transactions do you wish to add to the mempool? "
            ))
            if nb_of_new_transactions == 0:
                break

        except ValueError:
            print('We need a number here. Try again.')

    for i in range(nb_of_new_transactions):
        print(f'\nAdding transaction #{i + 1}\n')
        sender = input('sender: ')
        receiver = input('receiver: ')
        amount = input('amount: ')
        new_transaction = dict(
            sender=sender,
            receiver=receiver,
            amount=amount,
        )
        mempool.append(new_transaction)

    if len(mempool) > 0:
        blockchain.add_block(mempool)
        print('\nBlock added to blockchain.')
        print(f'Proof: {blockchain.chain[-1].proof}\n')

    write_blockchain_to_file(FILENAME, blockchain)


def read_blockchain_from_file(filename):
    """Read a textfile and parse it into a new blockchain.
    Return the blockchain.
    """

    blockchain = Blockchain()

    # TODO: handle when file is empty

    # empty the blockchain because we're adding all the values from file.
    blockchain.chain.clear()

    with open(filename, 'r') as bc_file:
        # One block has 8 lines, the first and last being the separators
        for line_nb, line in enumerate(bc_file.readlines()):
            if line_nb % 8 == 0:
                # separator
                pass
            elif line_nb % 8 == 1:
                # Here we get the block number and we create the Block
                block_nb = line_nb // 8
                blockchain.chain.append(Block({}, '0'))
            # For the next few lines we replace the Block attributes by the
            # appropiate values. For each line we ommit the last char, (\n).
            elif line_nb % 8 == 2:
                blockchain.chain[block_nb].timestamp = line[:-1]
            elif line_nb % 8 == 3:
                blockchain.chain[block_nb].transactions = line[:-1]
            elif line_nb % 8 == 4:
                blockchain.chain[block_nb].hash = line[:-1]
            elif line_nb % 8 == 5:
                blockchain.chain[block_nb].previous_hash = line[:-1]
            elif line_nb % 8 == 6:
                blockchain.chain[block_nb].proof = line[:-1]
            elif line_nb % 8 == 7:
                # separator
                pass

    print('Blockchain loaded.')

    return blockchain


def write_blockchain_to_file(filename, blockchain):
    """Write each block of the blockchain one after the other in a textfile."""

    with open(filename, 'w') as bc_file:
        blockchain_contents = [
            dict(
                block_index=i,
                timestamp=str(block.timestamp),
                transactions=block.transactions,
                hash=block.hash,
                previous_hash=block.previous_hash,
                proof=block.proof,
            )
            for i, block in enumerate(blockchain.chain)
        ]

        bc_file.write(
            json.dumps(blockchain_contents, indent=4, sort_keys=True)
        )


if __name__ == '__main__':
    main()
