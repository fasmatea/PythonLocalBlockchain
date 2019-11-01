#!/usr/bin/python3

"""Mini blockchain using Python."""

from blockchain import Blockchain


def main():
    """main function"""

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

    # grab 3 transactions from the mempool to prepare them for block structure
    block_transactions = [mempool.pop(0) for i in range(3)]

    my_blockchain = Blockchain()
    my_blockchain.add_block(block_transactions)
    new_transactions = [
        {'amount': '30', 'sender': 'alice', 'receiver': 'bob'},
        {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}
    ]
    my_blockchain.add_block(new_transactions)
    my_blockchain.print_blocks()
    my_blockchain.validate_chain()
    print()
    print("Changed a transaction in Block 1.")
    my_blockchain.chain[1].transactions = "fake_transactions"
    print()
    my_blockchain.validate_chain()

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
