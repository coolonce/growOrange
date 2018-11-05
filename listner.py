#!/usr/bin/python
import serial
import time
import json
import decimal
import io
import urllib3
from daemon import runner

class App():
    def __init__(self):
        self.stdin_path = '/dev/ttyUSB0'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_ptimeout = 5
    def run(self):
        while True:
            time.sleep(4)
            ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=4)
            sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))
            ser.isOpen()
            sio.flush()
            out = sio.readline()
            print(out)
            if out != '':
                http = urllib3.PoolManager()
#	            r = http.request('POST', 'http://lerts91.fvds.ru/api/sendData',body=out, headers = {'Content-Type':'application/json'})
#                print(r.data)


app = App()
daemon_run = runner.DaemonRunner(app)
daemon_run.do_action()
