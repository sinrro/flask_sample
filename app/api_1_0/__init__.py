from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api_1_0')

from . import test_api
