# -*- coding: UTF-8 -*-
import os
import json
import sys
import time
from task import Task
task_arr = []
if len(sys.argv)==2:
    if sys.argv[1]=="-d":
        bbr_task = Task("ls -l | grep bbr.sh")
        task_arr.append(Task("yum install python-setuptools && easy_install pip "))
        task_arr.append(Task("yum install m2crypto "))
        task_arr.append(Task("pip install shadowsocks "))
        task_arr.append(Task("pip install flask "))
        user_file = open("user.json")
        user_list = json.load(user_file)
        user_json = json.dumps(user_list)
        p1 = open("/etc/shadowsocks.json",'w')
        try:
            print "正在写入user——json"
            p1.write(user_json)
            p1.close()
            task_arr.append(Task("/usr/bin/ssserver -c /etc/shadowsocks.json -d start"))
            task_arr.append(Task("yum install firewalld"))
            task_arr.append(Task("systemctl start firewalld"))
            users = user_list["port_password"]
            for port in users:
                #print(users[port])
                task_arr.append(Task("firewall-cmd --permanent --zone=public --add-port="+str(port)+"/tcp"))
            task_arr.append(Task("firewall-cmd --permanent --zone=public --add-port=80/tcp"))
            task_arr.append(Task("firewall-cmd --permanent --zone=public --add-port=443/tcp"))
            task_arr.append(Task("firewall-cmd --reload"))
            task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d stop"))
            time.sleep(1)
            task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d start"))
            task_arr.append(Task("sudo wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh"))

        except Exception as e :
            print "发生预期之外的错误┭┮﹏┭┮"
            print(e)
    elif sys.argv[1]=="-r":
        task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d stop"))
        time.sleep(1)
        task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d start"))
    elif sys.argv[1]=="-server":
        print '正在开启server模式'
        from server import app
        app.run(host='0.0.0.0',port=80,debug=True)
    elif sys.argv[1]=="help" or sys.argv[1]=="-h" :
        print '-d：重新部署，-r：重启ss，-server：启动ssweb服务器，-help 帮助模式'
else:
    print '请输入正确的参数'
