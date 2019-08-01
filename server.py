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
        users = json.load(p1)
        print(users)
        try:
            for user in users:
                if user["username"] == username and user["password"] == password:
                    print("1000")
                    return "1000"
        except Exception as e :
            print(e)
            return "1001"
        return "1001"
@app.route('/admin',methods=['GET', 'POST'])
def admin():
    p1 = open("/etc/shadowsocks.json")
    users = json.load(p1)["port_password"]
    return render_template('admin.html',title='admin',users=users)
@app.route('/user',method=["POST","GET"])
def user():
    return render_template('user.html',title='admin',users=users)
@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        password =   request.form['password']
        file = open('data.json','r')
        try:
            data_json = json.load(file)
            for user in data_json:
                if user["username"]==username:
                    return "1002"
            data_dict = {}
            data_dict["username"] = username
            data_dict["password"] = password
            data_dict["port"] = str(8904+len(data_json))
            data_json.append(data_dict)
            data_json = json.dumps(data_json)
            file.close()
            file1 = open('data.json','w')
            file1.write(data_json)
            file1.close()
        except Exception as e:
            print(e)
            newdata = []
            data_dict = {}
            data_dict["username"] = username
            data_dict["password"] = password
            data_dict["port"] = 8904
            newdata.append(data_dict)
            data_json = json.dumps(newdata)
            file.close()
            file1 = open('data.json','w')
            file1.write(data_json)
            file1.close()

    return "1000"
