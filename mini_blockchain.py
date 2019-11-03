#!/usr/bin/python3

"""Mini blockchain using Python."""

from blockchain import Blockchain
from transactions import mempool


def main():
    """main function"""

    # prepare 100 transactions from the mempool for block structure
    block_transactions = [mempool.pop(0) for i in range(3)]

    my_blockchain = Blockchain()
    my_blockchain.add_block(block_transactions)

    # SUMMARY:

    block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
    block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
    block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}
    fake_transactions = {"sender": "Bob", "receiver": "Cole, Alice", "amount": "25"}

    local_blockchain = Blockchain()
    local_blockchain.print_blocks()
    local_blockchain.add_block(block_one_transactions)
    local_blockchain.add_block(block_two_transactions)
    local_blockchain.add_block(block_three_transactions)
    local_blockchain.print_blocks()
    local_blockchain.chain[2].transactions = fake_transactions
    local_blockchain.validate_chain()


if __name__ == "__main__":
    main()
