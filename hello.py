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


@app.route('/user/<username>')
def show_user_profile(username):
    #xian shi yong hu ming
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # 显示提交整型的用户"id"的结果，注意"int"是将输入的字符串形式转换为整型数据
    return 'Post {}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #显示/path/ 之后的路径名
    return 'Subpath {}'.format(subpath)

