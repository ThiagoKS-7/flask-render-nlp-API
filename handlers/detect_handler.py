from datetime import datetime
import spacy

class DetectHandler:
    def __init__(self, collection, body):
        self.collection = collection
        self.body = body
    def handle_detection(self, usr:str, ratio:any, tokens:any) -> any:
        if tokens <= 0:
            return {
            "message":"Error! Not enough tokens.",
            "status": 401
            }
        tokens -= 1
        self.collection.update_one(
            {'Username': usr}, 
            {
                "$set": {
                "Similiarity": ratio,
                "Tokens": tokens,
                "UpdatedAt": datetime.now(),
                }
            }
        )
        return {
        "message":"Sentence successfully saved.",
        "Tokens": tokens,
        "status": 200,
        }
    def start(self) -> any:
        usr = self.body["username"]
        nlp = spacy.load("en_core_web_sm")
        ratio = nlp(self.body["text1"]).similarity(nlp(self.body["text2"]))
        
        if self.collection.find_one({'Username': usr})["Password"]:
            self.handle_detection(self.collection, usr, ratio, self.collection.find_one({'Username': usr})["Tokens"])
        return {
            "message":"Error! User or password incorrect.",
            "status": 400
            }
