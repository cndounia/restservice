from flask_restplus import Api
from .calculator import api as ns_calc


api = Api(title='RestService',
          description='A simple Rest-Service for demonstration purposes',
          version='1.0')

api.add_namespace(ns_calc)
