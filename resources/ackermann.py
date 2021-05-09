from collections import deque

from resources._base import BaseMathResource, logger


class Ackermann(BaseMathResource):
    def __init__(self):
        super(Ackermann, self).__init__()
        self._request_parser.add_argument('m', type=int, required=True, help='required as non-negative integer')

    @staticmethod
    def calculate(m, n):
        if m < 0 or n < 0:
            raise ValueError('m and n must be non-negative integers')

        logger.info(f'Calculating the Ackermann function for (m, n)=({m}, {n})')

        stack = deque([])
        stack.extend([m, n])

        while len(stack) > 1:
            n, m = stack.pop(), stack.pop()

            if m == 0:
                stack.append(n + 1)
            elif m == 1:
                stack.append(n + 2)
            elif m == 2:
                stack.append(2 * n + 3)
            elif m == 3:
                stack.append(2 ** (n + 3) - 3)
            elif n == 0:
                stack.extend([m - 1, 1])
            else:
                stack.extend([m - 1, m, n - 1])

        return stack[0]
