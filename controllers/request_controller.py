
from flask import Response
from handlers.register_handler import RegisterHandler
from handlers.detect_handler import DetectHandler



def checkPostedData(collection,body, functionName):
  if  all( s not in body for s in ['username', 'password']):
    return {
      "message": "Error: missing required parameter usr/pwd.",
      "status": 401
    }
    
  handlers = {
    "register": RegisterHandler(collection, body),
    "detect": DetectHandler(collection, body),
  }

  if functionName in handlers:
    return handlers[functionName].start()
  

def handleRequest(collection,body, routeName):
    try:  
      return  checkPostedData(collection,body, routeName)
    except Exception as e:
      return Response("Error!  " + str(e),status=400)