
import unittest

from Calculator import Calculator
from CsvReader import CsvReader



class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(self.calculator.result)
        print("^^^^^^^^Subtraction^^^^^^^^")

    def test_addition(self):
        test_data = CsvReader('/src/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(self.calculator.result)
        print("^^^^^^^^Addition^^^^^^^^")

    def test_multiplication(self):
        test_data = CsvReader('/src/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(self.calculator.result)
        print("^^^^^^^^Multiplication^^^^^^^^")

    def test_division(self):
        test_data = CsvReader('/src/Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

            print(self.calculator.result)
        print("^^^^^^^^Division^^^^^^^^")

    def test_square(self):
        test_data = CsvReader('/src/Square.csv').data
        for row in test_data:
            self.calculator.square(int(row['Value 1']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(self.calculator.result)
        print("^^^^^^^^Square^^^^^^^^")

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()