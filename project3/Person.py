""" Module for Person class"""


class Person:
    """ Either sender or reciever"""

    def __init__(self, cypher):
        self.cypher = cypher

    def set_key(self, key):
        """ Sets this persons key"""
        self.key = key

    def get_key(self):
        """ Return this persons key """
        return self.key

    def operate_cypher(self, message):
        """ Use key to either encode or decode message """
