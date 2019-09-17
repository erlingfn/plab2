"""Module for RSA class"""
from random import randint

from Cypher import Cypher
from utils.crypto_utils import (blocks_from_text, generate_random_prime,
                                modular_inverse, text_from_blocks)


class RSA(Cypher):
    """ Encodes message with RSA encryption"""

    def encode(self, message, key):
        public_key = key[0]
        message_as_blocks = blocks_from_text(message, 1)
        encrypted_message_as_block = list(
            map(lambda m: pow(m, public_key[1], public_key[0]), message_as_blocks))
        return encrypted_message_as_block

    def decode(self, message, key):
        private_key = key[1]
        message_as_blocks = message
        decrypted_message_as_blocks = list(
            map(lambda m: pow(m, private_key[1], private_key[0]), message_as_blocks))
        return text_from_blocks(decrypted_message_as_blocks, 16)

    def generate_keys(self):
        p = generate_random_prime(8)
        q = generate_random_prime(8)
        while p == q:
            p = generate_random_prime(8)
            q = generate_random_prime(8)

        n = p * q
        phi = (p-1) * (q-1)
        d = False
        while not d:
            e = randint(3, phi - 1)
            d = modular_inverse(e, phi)
        return (n, e), (n, d)
