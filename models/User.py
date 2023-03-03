from flask_restful import Resource
from flask import request
from controllers.request_controller import handle_request as handle
from database.connection import collection
class Register(Resource):
  def post(self):
    return handle(collection(),request.get_json(), 'register')

class GetUsers(Resource):
  def get(self):
    return handle(collection(),request.get_json(), 'get-users')

