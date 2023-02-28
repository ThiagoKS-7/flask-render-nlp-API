
from flask import Response
from handlers.register_handler import RegisterHandler
from handlers.detect_handler import DetectHandler

handlers = {
  "register": RegisterHandler,
  "detect": DetectHandler,
}

def checkPostedData(collection,body, functionName):
  if  all( s not in body for s in ['username', 'password']):
    return {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 401
    }

  if functionName in handlers:
    return handlers[functionName].start(collection, body)
  

def handleRequest(collection,body, routeName):
    try:  
      return  checkPostedData(collection,body, routeName)
    except Exception as e:
      return Response("Error!  " + str(e),status=400)