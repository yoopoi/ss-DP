# -*- coding: UTF-8 -*-
import os
class Task:
    def __init__(self,task_command):
        self.task_command = task_command
        self.ack = 0
        print '正在执行:'+task_command
        self.process_task()
    def process_task(self):
        self.ack = os.system(self.task_command)
        if self.ack==256:
            print '\033[1;33;43'
            print "task执行失败:"+self.task_command
            print '\033[0m'
        else:
            print '\033[1;31;40m'
            print "task执行成功:"+self.task_command
            print '\033[0m'
