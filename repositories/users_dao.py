

class UsersDao:
    def __init__(self, collection, body):
        self.collection = collection
        self.body = body
    def start(self) -> any:
        usr = self.body["username"]
        
        if self.collection.find_one({'Username': usr})["Password"]:
            tokens = self.collection.find_one({'Username': usr})["Tokens"]
            result = [{
                        "username":col["Username"],
                        "text1":col["Text1"],
                        "text2":col["Text2"],
                        "tokens":col["Tokens"],
                    } for col in self.collection.find({},{"Username":1, "Text1":1, "Text2":1, "Tokens":1})]
                    
            return {
                "message":"Data successfully retrieved.",
                "data": result,
                "Tokens": tokens,
                "status": 200,
            }
                
        return {
            "message":"Error! Wrong User or password",
            "status": 400
            }