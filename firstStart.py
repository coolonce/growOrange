#!/usr/bin/python
import os
import time
import subprocess
import requests
import re
import sys
import json

def getMyIP():
    try:
        res = requests.get('http://whatismyip.org')
        ip = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
        if ip !="":
            return ip
    except:
        pass
    return 0



try:
    file_ver = open('file_ver.info', 'r')
except Exception:
    file_ver = open('file_ver.info', 'w')
    file_ver.write('0')

file_ver.close()

sendCount = 0
def CreateDevice():
    resp = requests.post("http://lerts91.fvds.ru/api/device")
    if (resp.status_code == 500) and (sendCount < 20):
        time.sleep(5*sendCount)
        sendCount += 1
        CreateDevice()
    else:
        data = resp.json()
        return data

def CreateConfig(id):
    conf_file = open('/home/swpi/growOrange/latest/conf.h', 'w')
    txt = '#define ID '+ str(id) + '\r\n'+'#define HUMIDITY_MIN1 200\r\n#define HUMIDITY_MAX1 1050\r\n#define HUMIDITY_MIN2 200\r\n#define HUMIDITY_MAX2 1050\r\n#define SEND_DATA_TIME 2000\r\n#define TIME_ON_LED 100000\r\n'
    conf_file.write(txt)
    conf_file.close()


import socket
countDelay = 0
def checknetwork():
    accept = True
    while(accept):        
        print("check network")
        time.sleep(10)
        try:
            socket.gethostbyaddr('www.yandex.ru')
            accept = False
        except socket.gaierror:
            accept = True
    start()



f = open('file_ver.info', 'rw+a+')
def start():
    for line in f:
        if line == '0':
            data = {}
            data = CreateDevice()
            CreateConfig(data['id'])
            print("start update")
            print(os.path.abspath(os.curdir))
            time.sleep(60)
            requests.get('http://lerts91.fvds.ru/api/addip/'+getMyIP())
            codeCall = subprocess.call(["python", "/home/swpi/growOrange/update.py"])
            if codeCall == 0:
                subprocess.call(["/home/swpi/growOrange/install.sh"])        
            f.write(data['version'])
            print(codeCall)
        else:
            print('Upload new script')
#            time.sleep(60)
            codeCall = subprocess.call(["python", "/home/swpi/growOrange/update.py"])
            if codeCall == 0:
                subprocess.call(["/home/swpi/growOrange/install.sh"])
                subprocess.call(["python","/home/swpi/growOrange/listner.py"])


if __name__ == "__main__":
    checknetwork()
	
