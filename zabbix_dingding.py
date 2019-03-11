#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   typ431127@gmail.com
# My blog https://www.aityp.com

import requests
import json
import sys
import os
import time
import configparser

headers = {'Content-Type': 'application/json'}
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

config=configparser.ConfigParser()
config.read('/etc/zabbix/dingding.conf',encoding='utf-8')
log_dir = config.get('config','log_dir')
log_file = config.get('config','log_file')
api_url = config.get('config','webhook')

def log(info):
    #注意权限,否则写不进去日志
    file_path=log_dir + log_file
    if os.path.isdir(log_dir) == False:
        os.makedirs(log_dir)
    elif os.path.isfile(file_path) == False:
        f = open(file_path, 'a+')
    f = open(file_path,'a+')
    f.write(info)
    f.close()

def msg(text,user):
    json_text= {"msgtype": "text","text": {"content": text},"at": {"atMobiles": [user],"isAtAll": False}}
    r=requests.post(api_url,data=json.dumps(json_text),headers=headers).json()
    code = r["errcode"]
    if code == 0:
        log(time + ":消息发送成功 返回码:" + str(code) + "\n")
    else:
        log(time + ":消息发送失败 返回码:" + str(code) + "\n")
        exit(3)

if __name__ == '__main__':
    text = sys.argv[3]
    user = sys.argv[1]
    msg(text,user)
