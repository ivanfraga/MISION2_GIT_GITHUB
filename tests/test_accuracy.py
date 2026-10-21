import unittest
from src.metricas import accuracy


class TestAccuracy(unittest.TestCase):
    def test_accuracy_parcial(self):
        self.assertAlmostEqual(accuracy([1, 0, 1], [1, 1, 1]), 2 / 3)

    def test_accuracy_rechaza_listas_vacias(self):
        with self.assertRaises(ValueError):
            accuracy([], [])


if __name__ == "__main__":
    unittest.main()