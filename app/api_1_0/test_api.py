from . import api
from flask_restful import Api, Resource
from flask import jsonify

my_api = Api(api)


class TestApi(Resource):
    def get(self):
        return jsonify({'hello': 'world'})


my_api.add_resource(TestApi, '/test_api', endpoint='test_api')
