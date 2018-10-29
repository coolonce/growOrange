import serial
import time
import json
import decimal
import io
import urllib3

print("start listing")
def ReadSerial():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=4)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))
    ser.isOpen()
    sio.flush()
    out = sio.readline()
    print(out)
    if out != '':
        http = urllib3.PoolManager()
	r = http.request('POST', 'http://lerts91.fvds.ru/api/sendData',body=out, headers={'Content-Type':'application/json'})
        print(r.data)
#        data = json.loads(out)
#        sensors = data['sensors']
#        for sensor in sensors:
#            print(sensor['id'], sensor['data'])
#        temp = data['Temperature']
#        hydro = data['Hydro']
#        print(temp, hydro)
while 1:
    ReadSerial()
    time.sleep(4)
