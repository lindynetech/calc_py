import unittest
from  calculator import Calculator

class TestClaclulator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator(4, 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 20)

if __name__ == '__main__':
    unittest.main()