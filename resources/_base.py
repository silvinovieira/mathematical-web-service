from abc import abstractmethod
import time

from flask import Flask
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

app = Flask(__name__)
logger = app.logger


class BaseMathResource(Resource):
    def __init__(self):
        self._request_parser = RequestParser()
        self._request_parser.add_argument('n', type=int, required=True, help='required as non-negative integer')
        super(BaseMathResource, self).__init__()

    def get(self):
        query_args = self._request_parser.parse_args()
        logger.info(f'[{self._get_class_name()}-ARGS] {query_args}')
        start_time = time.time()

        try:
            result = self.calculate(**query_args)
        except ValueError as err:
            logger.error(f'[{self._get_class_name()}-ERROR] {err}')
            return {'message': str(err)}, 400

        calc_time = time.time() - start_time
        logger.info(f'[{self._get_class_name()}-CALC-TIME] Calculated in {calc_time}s')
        logger.info(f'[{self._get_class_name()}-CALC-RES] The result is {result}')
        return {'result': result}

    @abstractmethod
    def calculate(self, **kwargs):
        pass

    def _get_class_name(self):
        return self.__class__.__name__.upper()
