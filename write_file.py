# adapted from https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython

import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import csv
from datetime import datetime

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0-5
channel_0 = AnalogIn(mcp, MCP.P0)
channel_1 = AnalogIn(mcp, MCP.P1)
channel_2 = AnalogIn(mcp, MCP.P2)
channel_3 = AnalogIn(mcp, MCP.P3)
channel_4 = AnalogIn(mcp, MCP.P4)
#channel_5 = AnalogIn(mcp, MCP.P5)


i = 3509

#writing data to csv file
while True:
    with open('poschair.csv', mode='a') as poschair_file:
        poschair_writer = csv.writer(poschair_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        datetime_obj = datetime.now()
        poschair_writer.writerow([i, datetime_obj,"Ch0", channel_0.value, channel_0.voltage, "Ch1",  channel_1.value, channel_1.voltage,
"Ch2",  channel_2.value, channel_2.voltage, "Ch3", channel_3.value, channel_3.voltage, "Ch4", channel_4.value, channel_4.voltage, "lean backward"])
        print(i, datetime_obj, channel_0.value, channel_0.voltage, channel_1.value, channel_1.voltage, channel_2.value, channel_2.voltage, channel_3.value, channel_3.voltage, channel_4.value, channel_4.voltage)
        #print('Written row ' + str(i) + ' on ' + str(datetime_obj))
        time.sleep(1)
        i += 1


        
        

#print values from each channel every 10 seconds
#while True:
#    for i in range(6):
#        print('Channel ' + str(i) + ' Raw Value: ', eval("channel_" + str(i) +".value"))
#        print('Channel ' + str(i) + ' ADC Voltage: ' + str(eval("channel_" + str(i) +".voltage")) + 'V')
#    time.sleep(10)
#    print('------------------')



