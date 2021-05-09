from resources._base import BaseMathResource, logger


class Fibonacci(BaseMathResource):
    def __init__(self):
        super(Fibonacci, self).__init__()

    @staticmethod
    def calculate(n):
        if n < 0:
            raise ValueError('n must be a non-negative integer')

        logger.info(f'Calculating Fibonacci for n={n}')

        if n in (0, 1):
            fibonacci = n
        else:
            latest_numbers = (0, 1)
            for _ in range(n - 1):
                nth = sum(latest_numbers)
                latest_numbers = (latest_numbers[-1], nth)
            fibonacci = latest_numbers[-1]
        return fibonacci
