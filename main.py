# -*- coding: UTF-8 -*-
import os
import json
from task import Task
task_arr = []
task_arr.append(Task("yum install python-setuptools && easy_install pip"))
task_arr.append(Task("yum install m2crypto"))
task_arr.append(Task("pip install shadowsocks"))
user_file = open("user.json")
p1 = open("/etc/shadowsocks.json",'w')
try:
    print "正在写入user——json"
    p1.write(user_file)
    p1.close()
except :
    print "写入json失败"
user_list = json.load(user_file)
task_arr.append(Task("/usr/bin/ssserver -c /etc/shadowsocks.json -d start"))
task_arr.append(Task("yum install firewalld"))
task_arr.append(Task("systemctl start firewalld"))
users = user_list["port_password"]
for port in users:
    #print(users[port])
    task_arr.append(Task("firewall-cmd --permanent --zone=public --add-port="+str(port)+"/tcp"))
    task_arr.append(Task("firewall-cmd --reload"))
