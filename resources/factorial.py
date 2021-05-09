from resources._base import BaseMathResource


class Factorial(BaseMathResource):
    def __init__(self):
        super(Factorial, self).__init__()

    @staticmethod
    def calculate(n):
        factorial = 1
        if n != 0:
            for i in range(1, n + 1):
                factorial *= i
        return factorial
