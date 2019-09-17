""" Module for Affine class"""

from Caesar import Caesar
from Cypher import Cypher
from Multiplication import Multiplication


class Affine(Cypher):
    """ Affine encrypts a message by first using Multiplication, then Caesar"""
    Caesar_help = Caesar()
    Multiplication_help = Multiplication()

    def encode(self, message, key):
        return Affine.Caesar_help.encode(
            Affine.Multiplication_help.encode(message, key[0]), key[1])

    def decode(self, message, key):
        return Affine.Multiplication_help.decode(Affine.Caesar_help.decode(message, key[1]), key[0])

    def generate_keys(self):
        return (Affine.Multiplication_help.generate_keys(), Affine.Caesar_help.generate_keys())

    def valid_keys(self):
        return (Affine.Multiplication_help.valid_keys(), Affine.Caesar_help.valid_keys())
