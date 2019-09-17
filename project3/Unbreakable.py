""" Module for Unbreakable class"""

from random import choice, randint

from Cypher import Cypher


class Unbreakable(Cypher):
    """ Encodes the message by adding it together with another string """

    def __init__(self, file_path):
        self.valid_words = read_from_file(file_path)

    def encode(self, message, key):
        new_key = create_key(message, key)
        encoded_message = ""
        for character1, char2 in zip(message, new_key):
            val = super().alphabet.index(character1)
            val += super().alphabet.index(char2)
            if val >= super().alphabet_len:
                val = val % super().alphabet_len
            encoded_message += super().alphabet[val]

        return encoded_message

    def decode(self, message, key):
        new_key = create_key(message, key)
        decode_key = ""
        for character in new_key:
            val = super().alphabet.index(character)
            val = super().alphabet_len - val % super().alphabet_len
            decode_key += super().alphabet[val]
        decoded_message = self.encode(message, decode_key)
        return decoded_message

    def generate_keys(self):
        return self.valid_words[randint(0, len(self.valid_words))]

    def valid_keys(self):
        return self.valid_words


def add_two_lists(list1, list2):
    """ Return a new list where each element is a combination
    of equivalent elements in the parameters """
    return list(map(lambda m: m[0] + m[1], list(zip(list1, list2))))


def create_key(message, key):
    """ Repeat key until same length as message """
    if len(key) > len(message):
        return key[0:len(message)]
    new_key = key * int(len(message)/len(key))
    new_key += key[0:len(message) - len(new_key)]
    return new_key


def read_from_file(file_path):
    f = open(file_path, "r")
    f1 = f.readlines()
    lines = list(map(lambda m: m.rstrip(), f1))
    return lines
