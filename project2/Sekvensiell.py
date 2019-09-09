from Spiller import Spiller
from Aksjon import Aksjon


class Sekvensiell(Spiller):
    """ Player class the sequence stein, saks, papir continuasly"""

    sekvens = ["stein", "saks", "papir"]

    def __init__(self, name):
        Spiller.__init__(self, name)
        self.sekvens_tall = -1

    def velg_aksjon(self):
        self.sekvens_tall += 1
        return Aksjon(Sekvensiell.sekvens[self.sekvens_tall % 3])
