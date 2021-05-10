from resources._base import BaseMathResource, logger


class Fibonacci(BaseMathResource):
    @staticmethod
    def calculate(n):
        if n < 0:
            raise ValueError('n must be a non-negative integer')

        if n in (0, 1):
            fibonacci = n
        else:
            latest_numbers = (0, 1)
            for i in range(2, n + 1):
                fibonacci_i = sum(latest_numbers)
                latest_numbers = (latest_numbers[-1], fibonacci_i)
                logger.debug(f'fibonacci({i}) = {fibonacci_i}')
            fibonacci = latest_numbers[-1]
        return fibonacci
