""" Module for Caesar class """
from random import randint

from Cypher import Cypher


class Caesar(Cypher):
    """ Ceaser Cypher encrypts a message by moving
    every char x steps to the right in the alphabet """

    def encode(self, message, key):

        encoded_message = ""
        for character in message:
            val = super().alphabet.index(character)
            val += key
            if val >= super().alphabet_len:
                val = val % super().alphabet_len
            encoded_message += super().alphabet[val]

        return encoded_message

    def decode(self, message, key):

        decoded_message = ""
        for character in message:
            val = super().alphabet.index(character)
            val -= key
            if val < 0:
                val += super().alphabet_len
            decoded_message += super().alphabet[val]

        return decoded_message

    def generate_keys(self):
        return randint(0, super().alphabet_len - 1)

    def valid_keys(self):
        """Return what is valid keys"""
        return range(0, super().alphabet_len)
