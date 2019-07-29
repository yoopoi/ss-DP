# -*- coding: UTF-8 -*-
import os
import json
import time
from task import Task
task_arr = []
task_arr.append(Task("yum install python-setuptools && easy_install pip "))
task_arr.append(Task("yum install m2crypto "))
task_arr.append(Task("pip install shadowsocks "))
user_file = open("user.json")
user_list = json.load(user_file)
user_json = json.dumps(user_list)
p1 = open("/etc/shadowsocks.json",'w')
try:
    print "正在写入user——json"
    p1.write(user_json)
    p1.close()
except Exception as e :
    print "写入json失败"
    print(e)

task_arr.append(Task("/usr/bin/ssserver -c /etc/shadowsocks.json -d start"))
task_arr.append(Task("yum install firewalld"))
task_arr.append(Task("systemctl start firewalld"))
users = user_list["port_password"]
for port in users:
    #print(users[port])
    task_arr.append(Task("firewall-cmd --permanent --zone=public --add-port="+str(port)+"/tcp"))
    task_arr.append(Task("firewall-cmd --reload"))
task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d stop"))
time.sleep(1)
task_arr.append(Task("ssserver -c /etc/shadowsocks.json -d start"))
task_arr.append(Task("sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org"))
task_arr.append(Task("sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm"))
task_arr.append(Task("sudo yum --enablerepo=elrepo-kernel install kernel-ml -y"))
task_arr.append(Task("rpm -qa | grep kernel"))
task_arr.append(Task("sudo egrep ^menuentry /etc/grub2.cfg | cut -f 2 -d \'"))
task_arr.append(Task("sudo grub2-set-default 1"))
