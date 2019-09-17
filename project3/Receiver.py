""" Module for Receiver class"""
from Person import Person


class Receiver(Person):
    """ Person receiving the encrypted message """

    def operate_cypher(self, message):
        return self.cypher.decode(message, self.get_key())
