# -*- coding: UTF-8 -*-
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
        if username == "admin" and password == "123":
            return "ok"
        print(username,password)
        p1 = open("/etc/shadowsocks.json")
        users = json.load(p1)["port_password"]
        for port in users:
            if port == username and users[port] == password:
                return "ok"
        return "fail"
@app.route('/admin',methods=['GET', 'POST'])
def admin():
    p1 = open("/etc/shadowsocks.json")
    users = json.load(p1)["port_password"]
    return render_template('admin.html',title='admin',users=users)
@app.route('/register',methods=['GET', 'POST'])
def register():
    return "comming soon!"
