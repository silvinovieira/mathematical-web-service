from abc import abstractmethod
import logging

from flask import Flask
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
logger = app.logger
logger.setLevel(logging.INFO)


class BaseMathResource(Resource):
    def __init__(self):
        self._request_parser = RequestParser()
        self._request_parser.add_argument('n', type=int, required=True, help='required as non-negative integer')
        super(BaseMathResource, self).__init__()

    def get(self):
        query_args = self._request_parser.parse_args()
        try:
            result = self.calculate(**query_args)
            return {'result': result}
        except ValueError as err:
            return {'message': str(err)}, 400

    @abstractmethod
    def calculate(self, **kwargs):
        pass
