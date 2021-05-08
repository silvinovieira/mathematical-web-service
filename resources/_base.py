from abc import abstractmethod

from flask_restful import Resource
from flask_restful.reqparse import RequestParser


class BaseMathResource(Resource):
    def __init__(self):
        self._request_parser = RequestParser()
        self._request_parser.add_argument('n', type=int, required=True, help='required as non-negative integer')
        super(BaseMathResource, self).__init__()

    @abstractmethod
    def calculate(self, *args):
        pass
