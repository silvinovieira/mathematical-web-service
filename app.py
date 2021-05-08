from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
api = Api(app, prefix='/api')


class Fibonacci(Resource):
    def __init__(self):
        self.__request_parser = RequestParser()
        self.__request_parser.add_argument(
            'n',
            type=int,
            required=True,
            help='The nth Fibonacci number is required as an integer',
        )
        super(Fibonacci, self).__init__()

    def get(self):
        args = self.__request_parser.parse_args()
        n = args['n']
        return self.calculate(n)

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


api.add_resource(Fibonacci, '/fibonacci')
