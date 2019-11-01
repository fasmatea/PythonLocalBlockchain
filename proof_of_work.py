#!/usr/bin/python3

"""Example of a simple Python script implementing blockchain mining."""

import hashlib


def main():
    """Main function."""

    block_content = b'Hello, let us try a string to emulate a blocks content!'
    search_hash = hashlib.sha256(block_content + bytes(0)).hexdigest()
    nonce = 0

    while not search_hash.startswith('0000'):
        search_hash = hashlib.sha256(block_content + bytes(nonce)).hexdigest()
        nonce += 1
        print(search_hash)

    print(nonce)


if __name__ == '__main__':
    main()
