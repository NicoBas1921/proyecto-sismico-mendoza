import math
import unittest

from proyecto_sismico_mendoza.magnitudes import to_mw


class MagnitudesTest(unittest.TestCase):
    def test_mw_directa_conserva_el_valor(self) -> None:
        result = to_mw(4.2, "Mw")
        self.assertEqual(result.mw, 4.2)
        self.assertEqual(result.method, "directa")

    def test_ml_usa_conversion_regional(self) -> None:
        result = to_mw(3.8, "ML")
        self.assertTrue(math.isclose(result.mw or 0, 0.97 * 3.8 + 0.1025))

    def test_mb_usa_conversion_definida(self) -> None:
        result = to_mw(4.1, "mb")
        self.assertTrue(math.isclose(result.mw or 0, 0.554 * 4.1 + 1.765))

    def test_tipo_no_admitido_preserva_trazabilidad(self) -> None:
        result = to_mw(3.5, "MG")
        self.assertIsNone(result.mw)
        self.assertEqual(result.original_value, 3.5)
        self.assertEqual(result.original_type, "MG")
        self.assertEqual(result.method, "sin_conversion")

    def test_rechaza_valores_no_finitos(self) -> None:
        with self.assertRaises(ValueError):
            to_mw(float("nan"), "Mw")


if __name__ == "__main__":
    unittest.main()
