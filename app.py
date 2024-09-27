# create a flask app
from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return "Hellow Heroku Lucho"

if __name__ == '__main__':
    app.run()

