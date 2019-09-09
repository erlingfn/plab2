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

        moenster = self.tidl_aksjoner[-self.husk]
        if not isinstance(moenster, list):
            moenster = [moenster]
        responser = []
        # Find all matching patterns of tidl_aksjoner
        for i in range(0, len(self.tidl_aksjoner) - self.husk):
            if self.tidl_aksjoner[i] == moenster[0]:
                if self.tidl_aksjoner[i:i + self.husk] == moenster:
                    responser.append(self.tidl_aksjoner[i + self.husk])
        # If no valid responses, return random
        if not responser:
            return velg_tilfeldig()

        return Aksjon(Spiller.Aksjonspar[most_frequent(responser)])

    def motta_resultat(self, self_action, opponent_action):
        self.tidl_aksjoner.append(opponent_action.action_type)


def velg_tilfeldig():
    """ Returns random Aksjon """
    return Aksjon(Spiller.action_types[randint(0, 2)])


def most_frequent(liste):
    """ Find most frequent value in list """
    counter = 0
    num = liste[0]

    for i in liste:
        curr_frequency = liste.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num
