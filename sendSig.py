import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
ser.write("1")
ser.close()