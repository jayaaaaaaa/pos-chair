from time import time, sleep
import main2
from urllib.request import urlopen
import sys
 
WRITE_API  = 'AUBE7IRHIFKUN4RZ' # PUT YOUR WRITE KEY HERE
BASE_URL = 'https://api.thingspeak.com/update?api_key={}'.format(WRITE_API)

SensorPrevSec = 0
SensorInterval = 16 # print data every 16 seconds
ThingSpeakPrevSec = 0
ThingSpeakInterval = 16 # send to Thingspeak every 16 seconds
 
try:
    while True:
        if time() - SensorPrevSec > SensorInterval:
            SensorPrevSec = time()
            ch0_value = round(main2.poschair()[0],2)
            ch1_value = round(main2.poschair()[2],2)
            ch2_value = round(main2.poschair()[4],2)
            ch3_value = round(main2.poschair()[6],2)
            ch4_value = round(main2.poschair()[8],2)
            print('ch0:', ch0_value, '     ch1:', ch1_value)
            print('ch2:', ch2_value, '     ch3:', ch3_value)
            print('ch4:', ch4_value)
        
        if time() - ThingSpeakPrevSec > ThingSpeakInterval:
            ThingSpeakPrevSec = time()
            
            thingspeakHttp = BASE_URL + '&field1' + str(ch0_value) + '&field2' + str(ch1_value) + '&field3' + str(ch2_value) + '&field4' + str(ch3_value)+ '&field5' + str(ch4_value)                      
            print(thingspeakHttp)
            
            conn = urlopen(thingspeakHttp)
            print('Response: {}'.format(conn.read()))
            conn.close()
            
            sleep(1)

except KeyboardInterrupt:
    conn.close()
