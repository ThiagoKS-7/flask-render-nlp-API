import bcrypt
from flask import Response
from datetime import datetime
import spacy

class DetectHandler:
    def __init__(self):
        pass
    def handle_detection(self, collection: any, usr:str, ratio:any, tokens:any) -> any:
        if tokens <= 0:
            return {
            "message":"Error! Not enough tokens.",
            "status": 401
            }
        tokens -= 1
        collection.update_one(
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
    def start(self, collection: any, body:any) -> any:
        usr = body["username"]
        nlp = spacy.load("en_core_web_sm")
        ratio = nlp(body["text1"]).similarity(nlp(body["text2"]))
        
        if collection.find_one({'Username': usr})["Password"]:
            self.handle_detection(collection, usr, ratio, collection.find_one({'Username': usr})["Tokens"])
        return {
            "message":"Error! User or password incorrect.",
            "status": 400
            }
