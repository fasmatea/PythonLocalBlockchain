"""This is supposed to be the more definitive version of the Blockchain,
ie. exporting it to a file each time it gets modified.
"""

from blockchain import Blockchain


def main():
    """Search in directory if blockchain file exists. If it doesn't, create the
    file and write a new Blockchain to it.

    Each time a block gets added to the blockchain, update the file, and
    validate its contents!
    """
