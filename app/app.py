from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    ''' Takes you home.'''
    return '<p>Hello, Cool person!</p>'

@app.route('/about-us')
def about():
    ''' Find more about us.'''
    return '<p>We are actually cooler than you think.</p>'
