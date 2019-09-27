""" Test module """
import unittest

from numpy import add, exp, multiply, sin

from calculator import Calculator
from containers import Queue, Stack
from functions import Function, Operator


class TestContainerMethods(unittest.TestCase):
    """ Test the methods of the container subclasses """

    def setUp(self):
        self.queue = Queue()
        self.stack = Stack()

    def test_size(self):
        """ Test size method """
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(self.queue.size(), 2)

        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 2)

    def test_is_empty(self):
        """ Test is_empty method """
        self.assertTrue(self.queue.is_empty())
        self.queue.push(2)
        self.assertFalse(self.queue.is_empty())

        self.assertTrue(self.stack.is_empty())
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        """ Test push method """
        self.queue.push(2)
        self.assertEqual(self.queue.peek(), 2)
        self.queue.push(3)
        self.queue.push(4)
        self.assertEqual(self.queue.peek(), 2)

        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.push(3)
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)

    def test_pop(self):
        """ Test pop method """
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), 3)
        self.assertTrue(self.queue.is_empty())

        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertTrue(self.stack.is_empty())


class TestFunctionsandOperators(unittest.TestCase):
    """ Test whether the function and operator classes work as expected """

    def test_func(self):
        """ Test if function class works as expected """
        exp_func = Function(exp)
        sin_func = Function(sin)
        self.assertEqual(exp_func.execute(sin_func.execute(0)), 1.0)

    def test_operator(self):
        """ Test if operator class works as expected """
        add_op = Operator(add, 0)
        multiply_op = Operator(multiply, 1)
        self.assertEqual(add_op.execute(1, multiply_op.execute(2, 3)), 7.0)


class TestCalculator(unittest.TestCase):
    """ Test main calculator class """

    def test_calc_init(self):
        """ Test that the calculator initiates successfully """
        calc = Calculator()
        self.assertEqual(calc.functions['COS'].execute(
            calc.operators['MINUS'].execute(6, calc.operators['GANGE'].execute(2, 3))), 1)

    def test_calc_execute_queue(self):
        """ Test that the calcuator executes a set of instructions correctly """
        calc = Calculator()
        calc.output_queue.push(1)
        calc.output_queue.push(2)
        calc.output_queue.push(3)
        calc.output_queue.push(calc.operators['GANGE'])
        calc.output_queue.push(calc.operators['PLUSS'])
        calc.output_queue.push(calc.functions['EXP'])
        self.assertEqual(round(calc.execute_instructions(), 2), 1096.63)

    def test_calc_refactor_to_rpn(self):
        """ Test calculators refactor_to_rpn method """
        calc = Calculator()
        calc.input_queue.push(calc.functions['EXP'])
        calc.input_queue.push('(')
        calc.input_queue.push(1)
        calc.input_queue.push(calc.operators['PLUSS'])
        calc.input_queue.push(2)
        calc.input_queue.push(calc.operators['GANGE'])
        calc.input_queue.push(3)
        calc.input_queue.push(')')
        calc.refactor_to_rpn()
        output_list = calc.output_queue._items + []
        self.assertListEqual(output_list, [
                             1, 2, 3, calc.operators['GANGE'],
                             calc.operators['PLUSS'], calc.functions['EXP']])

    def test_calc_text_parser(self):
        """ Tests the calculators text parser method """
        calc = Calculator()
        calc.text_parser("2 PLUSS 2")
        input_list = calc.input_queue._items + []
        self.assertListEqual(input_list, [2.0, calc.operators['PLUSS'], 2.0])

        # Empty the input_queue
        calc.input_queue = Queue()
        calc.text_parser("EXP(2 PLUSS 2)")
        input_list = calc.input_queue._items + []
        self.assertListEqual(
            input_list, [calc.functions['EXP'], '(', 2.0, calc.operators['PLUSS'], 2.0, ')'])

    def test_calc_full(self):
        """ Test the calcuator end to end """
        calc = Calculator()
        num = calc.calculate_expression("2 PLUSS 2")
        self.assertEqual(num, 4)

        num = calc.calculate_expression("2 PLUSS 2 GANGE 2")
        self.assertEqual(num, 6)

        num = calc.calculate_expression("EXP(2 PLUSS 2 GANGE 2)")
        self.assertEqual(round(num, 0), 403)

        num = calc.calculate_expression(
            "((15 DELE (7 MINUS (1 PLUSS 1))) GANGE 3) MINUS (2 PLUSS (1 PLUSS 1))")
        self.assertEqual(num, 5)


if __name__ == '__main__':
    unittest.main()
