from flask import Flask, render_template
from flask_restful import Api
from models.User import GetUsers, Register
from models.Nlp import Detect
from models.Tokens import Tokens

def api():
  return Api(app())

app = Flask(__name__)
api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(Detect, '/detect')
api.add_resource(GetUsers, '/get-users')
api.add_resource(Tokens, '/refill')

@app.route('/')
def hello_world():
  return render_template('index.html', title="Flask NLP REST API")


if __name__ == '__main__':
  app.run(debug=True)
