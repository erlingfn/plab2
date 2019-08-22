class Dog:

    #Class Attributes
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("My name is:", self.name)

    def get_age(self):
        return self.age


def get_biggest_number(*args):
    biggestNumber = 0
    for number in args:
        if number > biggestNumber:
            biggestNumber = number
    return biggestNumber


A = Dog("Goya", 10)
B = Dog("Ciao", 9)
C = Dog("Wixie", 5)

print("The oldest dog is",
      get_biggest_number(A.get_age(), B.get_age(), C.get_age()))
