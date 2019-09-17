""" Module for cypher class"""

import string
from abc import abstractmethod


class Cypher:
    """ Base class for different cyphers"""

    alphabet = string.printable.split("\t")[0]
    alphabet_len = len(alphabet)

    @abstractmethod
    def encode(self, message, key):
        """ Encode the message with the given key"""

    @abstractmethod
    def decode(self, message, key):
        """ Decode the message with the given key"""

    def verify(self, message, key):
        """ Verifies that the decoded message is the same as the original"""
        coded_message = self.encode(message, key)
        print(coded_message)  # For debug
        decoded_message = self.decode(coded_message, key)
        return message == decoded_message

    @abstractmethod
    def generate_keys(self):
        """ Generate keys for cypher"""
