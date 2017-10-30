#!/usr/bin/env python3
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
time=Time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

config=configparser.ConfigParser()
config.read('/etc/zabbix/dingding.conf')

log_file = config.get('config','log')
api_url = config.get('config','webhook')


def log(info):
    #注意权限,否则写不进去日志
    if os.path.isfile(log_file) == False:
               f = open(log_file, 'a+')

    f = open(log_file,'a+')
    f.write(info)
    f.close()

def msg(text,user):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                user
            ],
            "isAtAll": False
        }
    }

    r=requests.post(api_url,data=json.dumps(json_text),headers=headers)
    code=json.loads(r.content.decode())
    if code["errcode"] == 0:
        log(time + ":消息发送成功\n")
    else:
        log(time + ":消息发送失败" + r.content.decode("utf-8") + "\n")

if __name__ == '__main__':
    text = sys.argv[3]
    user = sys.argv[1]
    msg(text,user)
