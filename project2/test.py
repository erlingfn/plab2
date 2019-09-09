from Mangespill import *
from Tilfeldig import *
from Sekvensiell import *
from Mest_Vanlig import *
from Historiker import *

SPILL = Mangespill(Mest_Vanlig("Mest vanlig"),
                   Historiker("Historiker", 1), 1000)
SPILL.arranger_turnering()
