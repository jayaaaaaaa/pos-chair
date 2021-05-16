# adapted from https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython

import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

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
channel_5 = AnalogIn(mcp, MCP.P5)

#print values from each channel every 10 seconds
while True:
    for i in range(6):
        print('Channel ' + i + ' Raw Value: ', eval("channel_" + str(i) +".value"))
        print('Channel ' + i + ' ADC Voltage: ' + str(eval("channel_" + str(i) +".voltage")) + 'V')
    time.sleep(10)
