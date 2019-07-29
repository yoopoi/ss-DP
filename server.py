from flask import Flask
from flask import request
from flask import render_template
import json
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='login')
@app.route('/check',methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        username = request.form['name']
        password =   request.form['password']
        print(username,password)
        p1 = open("/etc/shadowsocks.json")
        users = json.load(p1)["port_password"]
        for port in users:
            if port == username and users[port] == password:
                return "ok"
        return "fail"
