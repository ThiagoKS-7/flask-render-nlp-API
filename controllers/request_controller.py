
from flask import Response
from handlers.register_handler import RegisterHandler
from handlers.detect_handler import DetectHandler


def checkPostedData(collection,body, functionName):
  if  all( s for s in ['username', 'password']) not in body:
    return {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 401
    }
  res = {
    "register": RegisterHandler(collection, body),
    "detect": DetectHandler(collection, body),
  }
  if functionName in res:
    return res[functionName]
  

def handleRequest(collection,body, routeName):
    try:  
      res = checkPostedData(collection,body, routeName)
      return res
    except Exception as e:
      error = Response("Error!  " + str(e),status=400)
      return error