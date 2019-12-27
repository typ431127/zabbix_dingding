#!/usr/bin/env python
# -*- coding: utf-8 -*-
# My blog https://www.aityp.com
# 此版本需要配置签名验证,只支持python3.x

import requests
import json
import sys
import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import configparser

headers = {'Content-Type': 'application/json'}
log_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
config=configparser.ConfigParser()
config.read('/etc/zabbix/dingding.conf',encoding='utf-8')
log_dir = config.get('config','log_dir')
log_file = config.get('config','log_file')
webhook = config.get('config','webhook')
secret = config.get('config','secret')

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
    timestamp = int(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    json_text= {"msgtype": "text","text": {"content": text},"at": {"atMobiles": [user],"isAtAll": False}}
    api_url = "%s&timestamp=%s&sign=%s" % (webhook.strip('\''),str(timestamp),sign)
    r=requests.post(api_url,data=json.dumps(json_text),headers=headers).json()
    code = r["errcode"]
    errmsg = r["errmsg"]
    if code == 0:
        log(log_time + ":消息发送成功 返回数据:%s %s\n" % (code,errmsg))
    else:
        log(log_time + ":消息发送失败 返回数据:%s %s\n" % (code,errmsg))
        print(log_time + ":消息发送失败 返回数据:%s %s\n" % (code,errmsg))
        exit(3)

if __name__ == '__main__':
    text = sys.argv[3]
    user = sys.argv[1]
    msg(text,user)
