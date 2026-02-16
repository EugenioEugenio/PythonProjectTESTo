from typing import Union

numeric = Union[int, float]


class Calculator:

    @staticmethod
    def add(a: numeric, b: numeric) -> numeric:
        return a + b

    @staticmethod
    def subtruct(a: numeric, b: numeric) -> numeric:
        return a - b

    @staticmethod
    def multiply(a: numeric, b: numeric) -> numeric:
        return a * b

    @staticmethod
    def divide(a: numeric, b: numeric) -> numeric:
        return a / b