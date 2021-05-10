from resources._base import BaseMathResource


class Factorial(BaseMathResource):
    @staticmethod
    def calculate(n):
        if n < 0:
            raise ValueError('n must be a non-negative integer')

        factorial = 1
        if n != 0:
            for i in range(1, n + 1):
                factorial *= i
        return factorial
