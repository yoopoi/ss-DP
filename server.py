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
        print(username,password)
        p1 = open("data.json")
        users = json.loads(p1)
        try:
            for user in users:
                if user["username"] == username and users["password"] == password:
                    return "1000"
        except :
            return "1001"
        return "1001"
@app.route('/admin',methods=['GET', 'POST'])
def admin():
    p1 = open("/etc/shadowsocks.json")
    users = json.load(p1)["port_password"]
    return render_template('admin.html',title='admin',users=users)
@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        password =   request.form['password']
        file = open('data.json','w')
        try:
            data_json = json.loads(file);
            for user in data_json:
                if user["username"]==username:
                    return "1001"
            data_dict = {}
            data_dict["username"] = username
            data_dict["password"] = password
            data_dict["port"] = 8904+len(data_json)
            data_json.append(data_dict)
            data_json = json.dumps(data)
            file.write(data_json)
            file.close()
        except:
            data = []
            data_dict = {}
            data_dict["username"] = username
            data_dict["password"] = password
            data_dict["port"] = 8904
            data.append(data_dict)
            data_json = json.dumps(data)
            file.write(data_json)
            file.close()

    return "comming soon!"
