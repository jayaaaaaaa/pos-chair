import thingspeak
import time
import main2
 
channel_id = 1396689 # PUT CHANNEL ID HERE
write_key  = 'AUBE7IRHIFKUN4RZ' # PUT YOUR WRITE KEY HERE
read_key   = 'T7GY095DRE310JYK' # PUT YOUR READ KEY HERE
 
def measure(channel):
    try:
        timenow = float(time.time())
        ch0_value = round(main2.poschair()[0],2)
        ch1_value = round(main2.poschair()[2],2)
        ch2_value = round(main2.poschair()[4],2)
        ch3_value = round(main2.poschair()[6],2)
        ch4_value = round(main2.poschair()[8],2)
        ch5_value = round(main2.poschair()[10],2)
        # write
        response = channel.update({'ch0_value': ch0_value, 'ch1_value': ch1_value,
        'ch2_value': ch2_value, 'ch3_value': ch3_value,
        'ch4_value': ch4_value, 'ch5_value': ch5_value,})
        
        # read
        read = channel.get({})
        print("Read:", read)
        
    except:
        print("connection failed")
 
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, write_key=write_key, api_key=read_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)
