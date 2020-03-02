import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        print("________Subtraction________")
        test_data = CsvReader('/src/csv/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(row['Value 2'], '-', row['Value 1'], '=', self.calculator.result)

    def test_addition(self):
        print("________Addition________")
        test_data = CsvReader('/src/csv/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(row['Value 2'], '+', row['Value 1'], '=', self.calculator.result)

    def test_multiplication(self):
        print("________Multiplication________")
        test_data = CsvReader('/src/csv/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(row['Value 2'], '*', row['Value 1'], '=', self.calculator.result)

    def test_division(self):
        print("________Division________")
        test_data = CsvReader('/src/csv/Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

            print(row['Value 2'], '/', row['Value 1'], '=', self.calculator.result)

    def test_square(self):
        print("________Square________")
        test_data = CsvReader('/src/csv/Square.csv').data
        for row in test_data:
            self.calculator.square(row['Value 1'])
            self.assertEqual(self.calculator.result, int(row['Result']))

            print(row['Value 1'], '^2', '=', self.calculator.result)

    def test_squareroot(self):
        print("________Square Root________")
        test_data = CsvReader('/src/csv/Square_Root.csv').data
        for row in test_data:
            self.calculator.sqroot(int(row['Value 1']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

            print('√', row['Value 1'], '=', self.calculator.result)


if __name__ == '__main__':
    unittest.main()
