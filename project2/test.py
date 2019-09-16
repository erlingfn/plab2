""" Testing module for running tournaments"""
from Historiker import Historiker
from Mangespill import Mangespill
from Mest_Vanlig import Mest_Vanlig
from Sekvensiell import Sekvensiell
from Tilfeldig import Tilfeldig

SPILLERE = {"Historiker": Historiker, "Tilfeldig": Tilfeldig,
            "Sekvensiell": Sekvensiell, "Mest_Vanlig": Mest_Vanlig}

ANTALL_SPILL = int(input("Velg antall spill: "))
SPILLER1 = input("Velg spiller1:")
if SPILLER1 == "Historiker":
    HUSK1 = int(input("Hvor mange skal den huske:"))
    SPILLER1_OBJEKT = SPILLERE[SPILLER1](SPILLER1, HUSK1)
else:
    SPILLER1_OBJEKT = SPILLERE[SPILLER1](SPILLER1)
SPILLER2 = input("Velg spiller2:")
if SPILLER2 == "Historiker":
    HUSK2 = int(input("Hvor mange skal den huske:"))
    SPILLER2_OBJEKT = SPILLERE[SPILLER2](SPILLER2, HUSK2)
else:
    SPILLER2_OBJEKT = SPILLERE[SPILLER2](SPILLER2)
SPILL = Mangespill(SPILLER1_OBJEKT,
                   SPILLER2_OBJEKT, ANTALL_SPILL)
SPILL.arranger_turnering()
