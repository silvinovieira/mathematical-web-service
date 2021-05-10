import logging

from flask import Flask
from flask_restful import Api

from resources import Ackermann, Factorial, Fibonacci

app = Flask(__name__)
api = Api(app, prefix='/api')

logging.basicConfig(filename='math-web-service.log', level=logging.INFO)

api.add_resource(Ackermann, '/ackermann')
api.add_resource(Factorial, '/factorial')
api.add_resource(Fibonacci, '/fibonacci')
