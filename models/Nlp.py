from flask_restful import Resource
from flask import request
from controllers.request_controller import handle_request as handle
from database.connection import collection as Nlp

'''
ARQUIVO QUE GERENCIA AS CLASSES USADAS NAS ROTAS
CHAMA O REPOSITÓRIO, QUE CUIDA DAS VALIDAÇÕES DA REQUEST
'''


class Detect(Resource):
  def patch(self):
    return handle(Nlp,request.get_json(), 'detect')
