""" Module for Sender class """
from Person import Person


class Sender(Person):
    """ Person sending the message"""

    def operate_cypher(self, message):
        return self.cypher.encode(message, self.get_key())
