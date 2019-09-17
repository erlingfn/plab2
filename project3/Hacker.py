""" Class for hacking the cyphers"""

from Person import Person
from Unbreakable import read_from_file


class Hacker(Person):
    """ Class that can brute force the different cyphers and check the answers"""

    def crack_cypher(self, encrypted_message, cypher):
        """ Crack message for a given cypher"""
        valid_keys = cypher.valid_keys()
        if(len(valid_keys) > 2):
            for key in valid_keys:
                decrypted_message = cypher.decode(encrypted_message, key)
                if check_string(decrypted_message):
                    return key
        else:
            valid1 = valid_keys[0]
            valid2 = valid_keys[1]
            for key1 in valid1:
                for key2 in valid2:
                    decrypted_message = cypher.decode(
                        encrypted_message, (key2, key1))
                    if check_string(decrypted_message):
                        return key2, key1

        print("Did not find valid_key")


valid_words = read_from_file("utils/english_words.txt")
valid_words_dict = {}
# populate dictionairy
for word in valid_words:
    valid_words_dict[word] = word


def check_string(message):
    words = message.split(" ")
    try:
        for word in words:
            print(valid_words_dict[word.lower()])
        return True
    except:
        return False
