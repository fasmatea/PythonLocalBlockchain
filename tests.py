"""All the test cases are listed here."""

import unittest
from blockchain import Blockchain


# TODO write following tests:


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

        self.assertEqual(self.blockchain.chain[0].previous_hash, 0)

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


if __name__ == '__main__':
    unittest.main()
