from flask import Flask
app = Flask(__name__)


#ru guo fang wen /,fan hui Index Page
@app.route('/')
def index():
    return 'Index Page'


#ru guo fang wen /hello,fan hui Hello, World!
@app.route('/hello')
def hello():
    return "Hello, World"



