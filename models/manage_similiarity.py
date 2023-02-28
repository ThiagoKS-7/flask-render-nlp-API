from pymongo import MongoClient
from flask_restful import Resource
from flask import request
from controllers.request_controller import handleRequest
import bcrypt
import os

'''
ARQUIVO QUE GERENCIA AS CLASSES USADAS NAS ROTAS
CHAMA O REPOSITÓRIO, QUE CUIDA DAS VALIDAÇÕES DA REQUEST
'''
path = f"mongodb+srv://{(os.environ.get('USER')).capitalize()}:<{os.environ.get('PASSWORD')}>@mymongo.otbi0bn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(path, 27017)
db = client.SimiliarityDatabase
# nova colecttion de nome Users
Users = db.Users

class Register(Resource):
  def post(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'register')
    return res

class Detect(Resource):
  def patch(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'detect')
    return res

class GetUsers(Resource):
  def get(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'get-users')
    return res

class Refill(Resource):
  def patch(self):
    body = request.get_json()
    if body:
      res = handleRequest(Users,body, 'refill')
    return res