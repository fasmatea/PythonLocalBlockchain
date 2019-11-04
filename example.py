#!/usr/bin/python3

"""Example implementation of a simple blockchain using Python."""

from blockchain import Blockchain
import mempool


def main():
    """Command line utility to see a simple blockchain in action."""

    # generate mempool with random values for 10 000 transactions
    local_mempool = mempool.create_mempool(10 * 1000)
    print('Mempool created.')

    input("...Show mempool >>>")

    for i, transaction in enumerate(local_mempool):
        print(f'Transaction {i + 1}:')
        print(f'  sender: {transaction["sender"]}')
        print(f'  receiver: {transaction["receiver"]}')
        print(f'  amount: {transaction["amount"]}')
        print()

    input("...Initalize Blockchain >>>")

    local_blockchain = Blockchain()
    print('Blockchain initialized.')
    local_blockchain.print_blocks()

    input("...Add blocks from mempool >>>")

    print('Adding blocks from the mempool...')

    while len(local_mempool) > 0:
        # prepare 100 transactions from the mempool for one block
        # the 100 transactions are removed from the mempool at the same time
        block_transactions = [local_mempool.pop(0) for i in range(100)]
        local_blockchain.add_block(block_transactions)
        print(f'Proof for block {len(local_blockchain.chain) - 1}: '
              f'{local_blockchain.chain[-1].proof}')

    input("...Show blocks >>>")
    local_blockchain.print_blocks()

    input("...Validate blockchain >>>")
    local_blockchain.validate_chain()

    input("...Modify a transaction >>>")

    fake_transactions = [{
        "sender": "Bob",
        "receiver": "Alice",
        "amount": "25",
    }]

    print("These transactions:\n")
    print(local_blockchain.chain[2].transactions)
    print('... were modified to:\n')
    print(fake_transactions)
    local_blockchain.chain[2].transactions = fake_transactions

    input("...Validate blockchain >>>")
    local_blockchain.validate_chain()


if __name__ == "__main__":
    main()
