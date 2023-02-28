#   elif functionName == 'get-users':
#     usr = body["username"]
#     pwd_exists = collection.find_one({'Username': usr})["Password"]
#     # se existe um password pra aquele user, é pq ele existe
#     if pwd_exists:
#       #faz update
#       tokens = collection.find_one({'Username': usr})["Tokens"]
#       # se o user tiver tokens, deixa passar
#       if tokens <= 0:
#         retJson = {
#           "message":"Error! Not enough tokens.",
#           "status": 401
#         }
#       else:
#         tokens = tokens -1
#         result = []
#         for col in collection.find({},{"Username":1, "Text1":1, "Text2":1, "Tokens":1}):
#           result.append({
#             "username":col["Username"],
#             "text1":col["Text1"],
#             "text2":col["Text2"],
#             "tokens":col["Tokens"],
#           })
        
#         retJson = {
#           "message":"Data successfully retrieved.",
#           "data": result,
#           "Tokens": tokens,
#           "status": 200,
#         }
#     else:
#       retJson = {
#       "message":"Error! User or password incorrect.",
#       "status": 400
#       }

#     return retJson

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