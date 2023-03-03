
from flask import Response
from repositories.register_dao import RegisterDao
from repositories.detect_dao import DetectDao
from repositories.users_dao import UsersDao



def check_data(collection,body, functionName):
  if  all( s not in body for s in ['username', 'password']):
    return {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 401
    }
    
  handlers = {
    "register": RegisterDao(collection, body),
    "detect": DetectDao(collection, body),
    "get-users": UsersDao(collection, body),
  }

  if functionName in handlers:
    return handlers[functionName].start()
  

def handle_request(collection,body, routeName):
    try:  
      return  check_data(collection,body, routeName)
    except Exception as e:
      return Response("Error!  " + str(e),status=400)