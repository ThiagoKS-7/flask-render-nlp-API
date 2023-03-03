import bcrypt
from datetime import datetime

class RegisterDao:
  def __init__(self, collection, body):
    self.collection = collection
    self.body = body
  
  def _handle_insert(self, data:any):
    self.collection.insert_one({
          "Username":data['usr'],
          "Password":data['hash_pwd'],
          "Text1":"",
          "Text2":"",
          "Similiarity":"", 
          "Tokens": 10,
          "CreatedAt": datetime.now(),
          "UpdatedAt":""
        })
    return {
    "message":"You successfully signed up!",
    "status": 200
    }

  def start(self) -> any:
      usr = self.body["username"]
      pwd = self.body["password"].encode('utf-8') # precisa passar com encode utf-8
      if not self.collection.find_one({'Username': usr}):
        self._handle_insert({'usr': usr, 'hash_pwd': bcrypt.hashpw(pwd, bcrypt.gensalt())})
      return {
        "message":"Error! User already exists.",
        "status": 400
      }