""" Testing module for running tournaments"""
from Historiker import Historiker
from Mangespill import Mangespill
from Mest_Vanlig import Mest_Vanlig

SPILL = Mangespill(Mest_Vanlig("Mest_Vanlig"),
                   Historiker("Historiker", 3), 100)
SPILL.arranger_turnering()
