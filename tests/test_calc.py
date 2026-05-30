import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from Calculadora import fatorial

class TestCalculadora(unittest.TestCase):
    def test_fatorial_de_5_deve_ser_120(self):
        self.assertEqual(fatorial(5), 120)

    def test_fatorial_de_0_deve_ser_1(self):
        self.assertEqual(fatorial(0), 1)

if __name__ == "__main__":
    unittest.main()