from flask import Flask,render_template
from flask_restful import Api 
from models.manage_similiarity import Register,Detect, GetUsers,Refill

app = Flask(__name__)
api =  Api(app)
 
title = "Flask NLP REST API"


'''
***********************
  *       API ROUTES    *
  ***********************
'''
api.add_resource(Register, '/register')
api.add_resource(Detect, '/detect')
api.add_resource(GetUsers, '/get-users')
api.add_resource(Refill, '/refill')

'''
***********************
*       APP ROUTES    *
***********************
'''
@app.route('/')
def hello_world():
  return render_template('index.html', title=title)


if __name__ == '__main__':
  app.run(debug=True)

