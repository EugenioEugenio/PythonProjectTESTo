import unittest

from app.calcul import Calculator


class TestCalcul(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_add_int(self):
        calcul = Calculator()
        a,b = 2,3
        expected_result=5
        actual_result = calcul.add(a,b)
        self.assertEqual(expected_result, actual_result)

    def test_sub_int(self):
        calcul = Calculator()
        a, b = 2, 3
        expected_result = -1
        actual_result = calcul.subtruct(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_mul_int(self):
        calcul = Calculator()
        a, b = 2, 3
        expected_result = 6
        actual_result = calcul.multiply(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_div_int(self):
        calcul = Calculator()
        a, b = 2, 3
        expected_result = 0.6666666666666666
        actual_result = calcul.divide(a, b)
        self.assertEqual(expected_result, actual_result)

    def test_safe_div_int(self):
        calcul = Calculator()
        a,b = 2,0

        expected_result = ZeroDivisionError
        with self.assertRaises(expected_result):
            calcul.divide(a,b)
