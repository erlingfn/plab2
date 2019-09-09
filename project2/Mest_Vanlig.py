from Spiller import Spiller
from Aksjon import Aksjon


class Mest_Vanlig(Spiller):
    """ Spiller class that chooses next action based on opponents most
    chosen common action """

    def __init__(self, name):
        Spiller.__init__(self, name)
        self.tidl_aksjoner = {"stein": 0, "saks": 0, "papir": 0}

    def velg_aksjon(self):
        vanligste_aksjon = max(self.tidl_aksjoner, key=self.tidl_aksjoner.get)
        return Aksjon(Spiller.Aksjonspar[vanligste_aksjon])

    def motta_resultat(self, self_action, opponent_action):
        self.tidl_aksjoner[str(opponent_action)] += 1
