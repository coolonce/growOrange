import os
from subprocess import Popen
import requests
import sys

try:
    file_ver = open('file_ver.info', 'r')
except Exception:
    file_ver = open('file_ver.info', 'w')
    file_ver.write('0')

file_ver.close()

f = open('file_ver.info', 'r')
for line in f:
    if line == '0':
        resp = requests.post("http://127.0.0.1:5000/api/device")
        print(resp)
#        Popen(["python", "update.py"])
