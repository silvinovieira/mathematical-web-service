from resources._base import BaseMathResource


class Fibonacci(BaseMathResource):
    def __init__(self):
        super(Fibonacci, self).__init__()

    def get(self):
        args = self._request_parser.parse_args()
        return self.calculate(args['n'])

    @staticmethod
    def calculate(n):
        if n in (0, 1):
            fibonacci = 1
        else:
            latest_numbers = (0, 1)
            for _ in range(n - 1):
                nth = sum(latest_numbers)
                latest_numbers = (latest_numbers[-1], nth)
            fibonacci = latest_numbers[-1]
        return fibonacci
