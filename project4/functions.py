""" Module for calculator functions"""

import numbers


class Function:
    """ Class for the calculator functions """

    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """ Execute assigned functions """
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        # Report
        if debug is True:
            print("Function: " + self.func.__name__ +
                  "({:f}) = {:f}".format(element, result))
        # Go home
        return result


class Operator():
    """ Class for calculator operators, i.e addition subtraction etc."""

    def __init__(self, operation, strength):
        self.operation = operation
        self.strength = strength

    def execute(self, element1, element2, debug=True):
        """ Execute assigned operation """
        if not (isinstance(element1, numbers.Number) or isinstance(element2, numbers.Number)):
            raise TypeError(
                "Cannot execute operationtions if elements are not numbers")

        result = self.operation(element1, element2)
        # Report
        if debug is True:
            print("{:f} {:s} {:f} equals {:f}".format(
                element1, self.operation.__name__, element2, result))

        return result
