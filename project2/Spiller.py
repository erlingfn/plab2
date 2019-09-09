class Spiller:
    """ Represents a player in rock paper scissor"""

    action_types = ["stein", "saks", "papir"]
    Aksjonspar = {"stein": "papir", "saks": "stein", "papir": "saks"}

    def __init__(self, name):
        self.name = name
        self.points = 0

    def velg_aksjon(self):
        """ Choose next action for player"""

    def motta_resultat(self, self_action, opponent_action):
        """ Recieve result from Enkeltspill """

    def oppgi_navn(self):
        return self.name
