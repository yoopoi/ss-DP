from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='login')
@app.route('/check',methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        username = request.args.get('name', '')
        password =  request.args.get('password', '')
        if username == "admin" and password == "123":
            return "ok"
        else:
            return "fail"
