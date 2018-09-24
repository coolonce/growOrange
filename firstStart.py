import os
from subprocess import Popen
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
        Popen(["python", "update.py"])
