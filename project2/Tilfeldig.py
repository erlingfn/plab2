from random import randint
from Aksjon import Aksjon
from Spiller import Spiller


class Tilfeldig(Spiller):
    def __init__(self, name):
        Spiller.__init__(self, name)

    def velg_aksjon(self):
        type_number = randint(0, 2)
        return Aksjon(Spiller.action_types[type_number])
