import logging

from flask import Flask
from flask_restful import Api

from resources import Ackermann, Factorial, Fibonacci
from resources.reports import LOG_FILE

app = Flask(__name__)
api = Api(app, prefix='/api')

if len(logging.getLogger().handlers) > 0:
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

api.add_resource(Ackermann, '/ackermann')
api.add_resource(Factorial, '/factorial')
api.add_resource(Fibonacci, '/fibonacci')
