""" Module for testing the project"""
from Affine import Affine
from Caesar import Caesar
from Hacker import Hacker
from Multiplication import Multiplication
from Receiver import Receiver
from RSA import RSA
from Sender import Sender
from Unbreakable import Unbreakable


def setup(cypher):
    """ setup function for testing """
    keys = cypher.generate_keys()
    sender = Sender(cypher)
    receiver = Receiver(cypher)
    hacker = Hacker(cypher)
    sender.set_key(keys)
    receiver.set_key(keys)
    return sender, receiver, hacker


def run_test(cypher):
    """ Run test"""
    while True:
        sender, receiver, hacker = setup(cypher)
        str_to_send = input("Hvilken streng vil du sende?")
        encrypted_message = sender.operate_cypher(str_to_send)
        key = hacker.crack_cypher(encrypted_message, hacker.cypher)
        decrypted_message = receiver.operate_cypher(encrypted_message)
        if key == sender.get_key():
            print("Found correct key", key)
            print("Message was", decrypted_message)


def demonstrate(cypher):
    """ demonstrate cypher """
    key = cypher.generate_keys()
    print(cypher.verify("This is a test", key))


CYP = Caesar()
CYP2 = Multiplication()
CYP3 = Affine()
CYP4 = Unbreakable("utils/english_words.txt")
CYP5 = RSA()
run_test(CYP4)
# demonstrate(CYP5)
