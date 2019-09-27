""" Module for the main calculator class """

import re
from numbers import Number

import numpy

from containers import Queue, Stack
from functions import Function, Operator


class Calculator:
    """ Main class for the calculator. Uses the postfix notation """

    def __init__(self):
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt)}
        self.operators = {'PLUSS': Operator(numpy.add, 0),
                          'GANGE': Operator(numpy.multiply, 1),
                          'DELE': Operator(numpy.divide, 1),
                          'MINUS': Operator(numpy.subtract, 0)}

        self.output_queue = Queue()
        self.input_queue = Queue()

    def execute_instructions(self):
        """ Execute the instructions in the output queue """
        temp_stack = Stack()

        while not self.output_queue.is_empty():
            element = self.output_queue.pop()
            if isinstance(element, Number):
                temp_stack.push(element)
            elif isinstance(element, Function):
                temp_stack.push(element.execute(temp_stack.pop()))
            elif isinstance(element, Operator):
                el1 = temp_stack.pop()
                el2 = temp_stack.pop()
                temp_stack.push(element.execute(el2, el1))

        return temp_stack.pop()

    def refactor_to_rpn(self):
        """ Refactor input_queue to rpn notation using the shunting-yard algorithm """
        operator_stack = Stack()

        while not self.input_queue.is_empty():
            element = self.input_queue.pop()
            if isinstance(element, Number):
                self.output_queue.push(element)
            elif isinstance(element, Function) or element == "(":
                operator_stack.push(element)
            elif element == ")":
                while operator_stack.peek() != "(":
                    temp_elem = operator_stack.pop()
                    self.output_queue.push(temp_elem)
                operator_stack.pop()

            elif isinstance(element, Operator):
                cont = not operator_stack.is_empty()
                while cont:
                    top_elem = operator_stack.peek()
                    if isinstance(top_elem, Function) or (
                            (isinstance(top_elem, Operator)
                             and top_elem.strength >= element.strength)):
                        self.output_queue.push(operator_stack.pop())
                    else:
                        cont = False

                operator_stack.push(element)

        while not operator_stack.is_empty():
            self.output_queue.push(operator_stack.pop())

    def text_parser(self, input_string):
        """Parses text into array of operators and operands """
        string = input_string.replace(" ", "").upper()
        target_nums = ("^[-0123456789.]+")
        target_funcs = "|".join(["^" + func for func in self.functions])
        target_ops = "|".join(["^" + op for op in self.operators])
        target_parenthesis = ("^[\(\)]")
        while string != "":
            check = re.search(target_nums, string)
            if check is not None:
                string = sub_string(string, check.end)
                self.input_queue.push(float(check.group(0)))

            check = re.search(target_funcs, string)
            if check is not None:
                string = sub_string(string, check.end)
                self.input_queue.push(self.functions[check.group(0)])

            check = re.search(target_ops, string)
            if check is not None:
                string = sub_string(string, check.end)
                self.input_queue.push(self.operators[check.group(0)])

            check = re.search(target_parenthesis, string)
            if check is not None:
                string = sub_string(string, check.end)
                self.input_queue.push(check.group(0))

    def calculate_expression(self, input_string):
        """ Calculate the given expression and return result """
        self.text_parser(input_string)
        self.refactor_to_rpn()
        return self.execute_instructions()


def sub_string(string, end):
    """ Helper funtion to substitute with an index in itself """
    if len(string)-1 < end(0):
        return ""
    return string[end(0):]
