#!/usr/bin/python3

"""Mini blockchain using Python."""

import time
from blockchain import Blockchain
import mempool


def main():
    """main function"""

    # generate mempool with random values for 10 000 transacations
    local_mempool = mempool.create_mempool(10 * 1000)
    print('Mempool created.')

    local_blockchain = Blockchain()
    print('Blockchain initialized.')
    local_blockchain.print_blocks()

    time.sleep(3)

    print('Adding blocks from the mempool...')
    time.sleep(2)

    while len(local_mempool) > 0:
        # prepare 100 transactions from the mempool for one block
        # the 100 transactions are removed from the mempool at the same time
        block_transactions = [local_mempool.pop(0) for i in range(100)]
        local_blockchain.add_block(block_transactions)
        local_blockchain.print_blocks()

    local_blockchain.validate_chain()

    time.sleep(3)

    fake_transactions = {
        "amount": "25",
        "sender": "Bob",
        "receiver": "Alice",
    }

    print('Modifying a transaction...')
    local_blockchain.chain[2].transactions = fake_transactions
    time.sleep(2)
    local_blockchain.validate_chain()


if __name__ == "__main__":
    main()
