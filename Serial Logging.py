import serial
import time
import urllib
import requests
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
baseURL = 'http://api.thingspeak.com/update?key=ADDYOURAPIHERE'

plt.close('all')
plt.figure()
plt.ion()
#Setup the serial port
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=1500000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = None
)

file_name = input("Please enter file name:")
data_file = open(file_name,'w')
data_file.write("Voltage data\n")
data_file.write("Time(HH:MM:SS) voltages(v)\n")

while 1:
		ser.write('GET'.encode())
		voltages= ser.read(600).hex()
		voltages = voltages.rstrip('EESS')
		voltages= voltages[:-1]    				 
		print (voltages)
		now = time.strftime("%H.%M.%S")
		y = str(now)
		data_file.write(y)
		data_file.write("")
		y=str(voltages)  
		data_file.write(y)
		data_file.write("\n")   
		f = requests.post(baseURL+'&field1=' +str(voltages))

		f.close()
    
