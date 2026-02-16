
import unittest

# 1. Функция, проверяющая, является ли число четным
def is_even(num):
    """Возвращает True, если число четное, и False в противном случае."""
    return num % 2 == 0

# 2. Класс для тестирования
class TestIsEven(unittest.TestCase):
    def test_is_even_parametrized(self):
        # Набор данных: (число, ожидаемый_результат)
        test_cases = [
            (2, True),      # Положительное четное
            (3, False),     # Положительное нечетное
            (0, True),      # Ноль
            (-2, True),     # Отрицательное четное
            (-5, False),    # Отрицательное нечетное
            (100, True),    # Большое четное
            (101, False),   # Большое нечетное
            (999999998, True),
            (999999999, False),
            (1.5, False),
        ]

        for num, expected in test_cases:
            # 3. Использование subTest для параметризации
            with self.subTest(num=num):
                self.assertEqual(is_even(num), expected, f"Failed for {num}")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)




