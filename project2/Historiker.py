""" Historian Class"""
from random import randint

from Aksjon import Aksjon
from Spiller import Spiller


class Historiker(Spiller):
    """ Spiller class that makes choices based on x amount of opponents previous
    actions """

    def __init__(self, name, husk):
        Spiller.__init__(self, name)
        self.husk = husk
        self.tidl_aksjoner = []

    def velg_aksjon(self):
        # If there is no history choose random action
        if len(self.tidl_aksjoner) <= self.husk + 1:
            return velg_tilfeldig()

        moenster = self.tidl_aksjoner[-self.husk:]
        responser = {"stein": 0, "saks": 0, "papir": 0}
        # Find all matching patterns of tidl_aksjoner
        for i in range(0, len(self.tidl_aksjoner) - self.husk):
            if self.tidl_aksjoner[i] == moenster[0]:
                if self.tidl_aksjoner[i:i + self.husk] == moenster:
                    responser[self.tidl_aksjoner[i + self.husk]] += 1

        neste_aksjon = max(responser, key=responser.get)

        return Aksjon(Spiller.Aksjonspar[neste_aksjon])

    def motta_resultat(self, self_action, opponent_action):
        self.tidl_aksjoner.append(opponent_action.action_type)


def velg_tilfeldig():
    """ Returns random Aksjon """
    return Aksjon(Spiller.action_types[randint(0, 2)])
