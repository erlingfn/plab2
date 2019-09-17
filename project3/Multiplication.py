""" Module for Multiplication class"""

from random import randint

from Cypher import Cypher
from utils.crypto_utils import modular_inverse


class Multiplication(Cypher):
    """ Multiplication cypher encrypts a message by moving
    every character by its postion * x places to the right"""

    def encode(self, message, key):
        encoded_message = ""
        for character in message:
            val = super().alphabet.index(character)

            val *= key
            if val >= super().alphabet_len:
                val = val % super().alphabet_len

            encoded_message += super().alphabet[val]

        return encoded_message

    def decode(self, message, key):

        decode_key = modular_inverse(key, super().alphabet_len)
        decoded_message = self.encode(message, decode_key)

        return decoded_message

    def generate_keys(self):
        return randint(1, 100)

    def valid_keys(self):
        return range(1, 100)
