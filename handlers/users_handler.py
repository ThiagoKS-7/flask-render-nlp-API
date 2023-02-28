

class UsersHandler:
    def __init__(self):
        pass
    def start(collection:any, body:any) -> any:
        usr = body["username"]
        
        if collection.find_one({'Username': usr})["Password"]:
            tokens = collection.find_one({'Username': usr})["Tokens"]
            if tokens <= 0:
                return {
                    "message":"Error! Not enough tokens.",
                    "status": 401
                }
            tokens -= 1
            result = [{
                        "username":col["Username"],
                        "text1":col["Text1"],
                        "text2":col["Text2"],
                        "tokens":col["Tokens"],
                    } for col in collection.find({},{"Username":1, "Text1":1, "Text2":1, "Tokens":1})]
                    
            return {
                "message":"Data successfully retrieved.",
                "data": result,
                "Tokens": tokens,
                "status": 200,
            }
                
        return {
            "message":"Error! User or password incorrect.",
            "status": 400
            }

#   elif functionName == 'refill':
#     usr = body["username"]
#     target=body["target"]
#     pwd = body["password"]
#     tokens = body["tokens"]
#     pwd_exists = collection.find_one({'Username': usr})["Password"]
#     #se existe um password pra aquele user, é pq ele existe
#     if pwd_exists and usr == 'admin':
#       #faz update
#       collection.update_one({'Username': target}, {"$set": {
#         "Tokens": tokens,
#         "UpdatedAt": datetime.now(),
#       }})
#       retJson = {
#         "message":"Sentence successfully saved.",
#         "Tokens": tokens,
#         "status": 200,
#       }
#     else:
#       retJson = {
#       "message":"Error! Only admin can refill tokens.",
#       "status": 400
#       }

#     return retJson