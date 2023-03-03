from flask_restful import Resource
from flask import request
from controllers.request_controller import handle_request as handle
from database.connection import collection as Users

class Tokens(Resource):
  def patch(self):
    return handle(
        Users,
        request.get_json(), 
        'refill'
      )