class Enkeltspill:
    """One round of rock-paper-scissor"""

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.string = ""

    def gjennomfoer_spill(self):
        """ Execute one round of rock-paper-scissor"""
        action1 = self.spiller1.velg_aksjon()
        self.string += self.spiller1.oppgi_navn() + ": " + str(action1) + " "
        action2 = self.spiller2.velg_aksjon()
        self.string += self.spiller2.oppgi_navn() + ": " + str(action2) + " "
        self.string += "-> "
        if action1 > action2:
            self.spiller1.points += 1
            self.string += self.spiller1.oppgi_navn() + " vant"
        if action1 == action2:
            self.spiller1.points += 0.5
            self.spiller2.points += 0.5
            self.string += " uavgjort"
        if action1 < action2:
            self.spiller2.points += 1
            self.string += self.spiller2.oppgi_navn() + " vant"

        self.spiller1.motta_resultat(action1, action2)
        self.spiller2.motta_resultat(action2, action1)

    def __str__(self):
        return self.string
