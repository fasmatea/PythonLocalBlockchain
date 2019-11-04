"""This is supposed to be the more definitive version of the Blockchain,
ie. exporting it to a file each time it gets modified.
"""

import os
from blockchain import Blockchain


def main():
    """Search in directory if blockchain file exists. If it doesn't, create the
    file and write a new Blockchain to it.

    Each time a block gets added to the blockchain, update the file, and
    validate its contents!
    """

    if 'written_blockchain' not in os.listdir():
        my_blockchain = Blockchain()
        with open('written_blockchain', 'a') as bc_file:
            for i, block in enumerate(my_blockchain.chain):
                bc_file.write('=====\n')
                bc_file.write(f'Block {i}:\n')
                bc_file.write(f'timestamp: {block.timestamp}\n')
                bc_file.write(f'transactions: {block.transactions}\n')
                bc_file.write(f'current hash: {block.hash}\n')
                bc_file.write(f'previous hash: {block.previous_hash}\n')
                bc_file.write(f'proof of work: {block.proof}\n')
                bc_file.write('=====\n')
        print('No blockchain was found, created new blockchain.')


if __name__ == '__main__':
    main()
