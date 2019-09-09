class Aksjon:
    action_types = ["stein", "saks", "papir"]

    def __init__(self, action_type):
        if not Aksjon.action_types.__contains__(action_type):
            return
        self.action_type = action_type

    def __eq__(self, other):
        if self.action_type == other.action_type:
            return True
        return False

    def __gt__(self, other):
        if self.action_type == "stein" and other.action_type == "saks":
            return True
        if self.action_type == "saks" and other.action_type == "papir":
            return True
        if self.action_type == "papir" and other.action_type == "stein":
            return True
        return False

    def __lt__(self, other):
        if self.action_type == "stein" and other.action_type == "papir":
            return True
        if self.action_type == "saks" and other.action_type == "stein":
            return True
        if self.action_type == "papir" and other.action_type == "saks":
            return True
        return False

    def __str__(self):
        return self.action_type
