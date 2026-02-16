
import unittest

# 1. Создание функции safe_divide
def safe_divide(a, b):
    """Делит a на b, возбуждает ZeroDivisionError при делении на ноль."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b

# 2. Создание теста для проверки исключения
class TestSafeDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        """Проверяет, что при делении на ноль возникает ZeroDivisionError."""
        # Используем assertRaises для проверки исключения
        with self.assertRaises(ZeroDivisionError):
            safe_divide(10, 0)

    def test_normal_division(self):
        """Проверяет корректное деление."""
        self.assertEqual(safe_divide(10, 2), 5.0)

if __name__ == '__main__':
    unittest.main()
