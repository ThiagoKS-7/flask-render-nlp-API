import bcrypt
from datetime import datetime

class RegisterHandler:
  
  def _handle_insert(self, collection:any, data:any):
    collection.insert_one({
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

  def start(self, collection:any, body:any) -> any:
      usr = body["username"]
      pwd = body["password"].encode('utf-8') # precisa passar com encode utf-8
      if not collection.find_one({'Username': usr}):
        self._handle_insert(collection, {'usr': usr, 'hash_pwd': bcrypt.hashpw(pwd, bcrypt.gensalt())})
      return {
        "message":"Error! User already exists.",
        "status": 400
      }