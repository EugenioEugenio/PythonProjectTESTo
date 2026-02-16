import unittest

from app.calcul import Calculator


class safeCalcul(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_safe_div_int(self):
        calcul = Calculator()
        a,b = 2,0

        expected_result =ZeroDivisionError
        with self.assertRaises(expected_result):
            calcul.divide(a,b)
