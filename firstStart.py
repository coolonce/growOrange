import os
import time
from subprocess import Popen
import requests
import re
import sys

def getMyIP():
    try:
        res = requests.get('http://whatismyip.org')
        ip = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
        if ip !="":
            return ip
    except:
        pass
    return 0

requests.get('http://127.0.0.1:5000/api/addip/'+getMyIP())

try:
    file_ver = open('file_ver.info', 'r')
except Exception:
    file_ver = open('file_ver.info', 'w')
    file_ver.write('0')

file_ver.close()

sendCount = 0
def CreateDevice():
    resp = requests.post("http://127.0.0.1:5000/api/device")
    if (resp.status_code == 500) and (sendCount < 20):
        time.sleep(5*sendCount)
        CreateDevice()
    else:
        data = json.loads(request.data.decode('utf-8'))
        return data

def CreateConfig(id):
    conf_file = open('latest/conf.h', 'w')
    txt = '#define ID '+ str(data['id']) + '\r\n'+'#define HUMIDITY_MIN1 200\r\n#define HUMIDITY_MAX1 1050\r\n#define HUMIDITY_MIN2 200\r\n#define HUMIDITY_MAX2 1050\r\n#define SEND_DATA_TIME 2000\r\n#define TIME_ON_LED 100000\r\n'
    conf_file.write(txt)
    conf_file.close()


f = open('file_ver.info', 'r')
for line in f:
    if line == '0':
        data = {}
#        data = CreateDevice()
        data['id'] = 2
        CreateConfig(data['id'])
#        Popen(["python", "update.py"])
