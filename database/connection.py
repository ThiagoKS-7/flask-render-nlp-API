from pymongo import MongoClient
from decouple import config

path = f"mongodb+srv://{(config('DB_USR'))}:{config('DB_PASSWORD')}@cluster0.8nqzucw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(path)
def db():
    return client.SimiliarityDatabase

def collection():
    return client.SimiliarityDatabase.Users