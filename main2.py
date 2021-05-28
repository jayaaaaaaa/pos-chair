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

#print values from each channel every 1 second
def poschair():
    ch0_value = channel_0.value
    ch0_voltage = channel_0.voltage
    ch1_value = channel_1.value
    ch1_voltage = channel_1.voltage
    ch2_value = channel_2.value
    ch2_voltage = channel_2.voltage
    ch3_value = channel_3.value
    ch3_voltage = channel_3.voltage
    ch4_value = channel_4.value
    ch4_voltage = channel_4.voltage
    return ch0_value, ch0_voltage, ch1_value, ch1_voltage, ch2_value, ch2_voltage, ch3_value, ch3_voltage, ch4_value, ch4_voltage
