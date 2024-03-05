from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    ''' Takes you home.'''
    return '<p>Hello, Cool person!</p>'
