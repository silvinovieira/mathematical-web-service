from resources._base import BaseMathResource


class Ackermann(BaseMathResource):
    def __init__(self):
        super(Ackermann, self).__init__()
        self._request_parser.add_argument('m', type=int, required=True, help='required as non-negative integer')

    @staticmethod
    def calculate(m, n):
        if m < 0 or n < 0:
            raise ValueError('m and n must be non-negative integers')

        stack = []
        while True:
            if not m:
                if not stack:
                    return n + 1
                m, n = stack.pop(), n + 1
            elif not n:
                m, n = m - 1, 1
            else:
                stack.append(m - 1)
                n -= 1
