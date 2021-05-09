from resources._base import BaseMathResource, logger


class Factorial(BaseMathResource):
    def __init__(self):
        super(Factorial, self).__init__()

    @staticmethod
    def calculate(n):
        if n < 0:
            raise ValueError('n must be a non-negative integer')

        logger.info(f'Calculating the factorial for n={n}')

        factorial = 1
        if n != 0:
            for i in range(1, n + 1):
                factorial *= i
        return factorial
