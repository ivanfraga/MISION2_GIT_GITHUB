import unittest
from src.predictor import entrenar_modelo, predecir_ejemplo


class TestPredictor(unittest.TestCase):
    def test_entrenar_modelo_devuelve_conjunto_de_prueba(self):
        modelo, x_test, y_test = entrenar_modelo()
        self.assertEqual(len(x_test), len(y_test))
        self.assertGreater(len(x_test), 0)

    def test_predecir_ejemplo_devuelve_enteros_validos(self):
        predicho, real = predecir_ejemplo()
        self.assertIsInstance(predicho, int)
        self.assertIsInstance(real, int)
        self.assertIn(predicho, (0, 1, 2))
        self.assertIn(real, (0, 1, 2))


if __name__ == "__main__":
    unittest.main()