from flask_restful import Resource
from flask_restful.reqparse import RequestParser


class Ackermann(Resource):
    def __init__(self):
        self.__request_parser = RequestParser()
        self.__request_parser.add_argument('m', type=int, required=True, help='required as non-negative integer')
        self.__request_parser.add_argument('n', type=int, required=True, help='required as non-negative integer')
        super(Ackermann, self).__init__()

    def get(self):
        args = self.__request_parser.parse_args()
        return self.calculate(args['m'], args['n'])

    @staticmethod
    def calculate(m, n):
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
