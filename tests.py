"""All the test cases are listed here."""

import unittest
from random import randint
import mempool
from blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    """TestCase for Blockchains."""

    def test_initialize_blockchain(self):
        """Initializing empty blockchain should create genesis block."""

        blockchain = Blockchain()

        self.assertEqual(len(blockchain.chain), 1)


class TestBlock(unittest.TestCase):
    """TestCase for Blocks."""

    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block_has_previous_hash_of_0(self):
        """Genesis block should have a previous hash of 0."""

        self.assertEqual(self.blockchain.chain[0].previous_hash, '0')

    def test_block_proof_starts_with_difficulty_zeros(self):
        """Block proof should always start with {difficulty} zeros."""

        # We will test it with 10 blocks:
        for i in range(10):
            self.blockchain.add_block('test transaction')
            self.assertTrue(
                self.blockchain.chain[i + 1].proof.startswith(
                    '0' * self.blockchain.proof_difficulty
                )
            )


class TestMempool(unittest.TestCase):
    """TestCase for the mempool."""

    NB_TRANSACTIONS = randint(0, 10 * 1000)

    def setUp(self):
        self.test_mempool = mempool.create_mempool(self.NB_TRANSACTIONS)

    def test_mempool_type(self):
        """The mempool should be a list."""

        self.assertIs(type(self.test_mempool), list)

    def test_mempool_size(self):
        """The mempool should contain the correct number of transactions."""

        self.assertEqual(len(self.test_mempool), self.NB_TRANSACTIONS)


if __name__ == '__main__':
    unittest.main()
