from time import time, sleep
import main2
import tree_model
from urllib.request import urlopen
import sys

WRITE_API = 'AUBE7IRHIFKUN4RZ'  # PUT YOUR WRITE KEY HERE
BASE_URL = 'https://api.thingspeak.com/update?api_key={}'.format(WRITE_API)

SensorPrevSec = 0
SensorInterval = 16  # print data every 16 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 16  # send to Thingspeak every 16 seconds

try:
    while True:
        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            posture = tree_output
            print('result: ', posture)

        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()

            thingspeakHttp = BASE_URL + '&field1' + str(posture)
            print(thingspeakHttp)

            conn = urlopen(thingspeakHttp)
            print('Response: {}'.format(conn.read()))
            conn.close()

            sleep(1)

except KeyboardInterrupt:
    conn.close()
