from google.cloud import pubsub_v1
import datetime
import json
import main2
import time
 
project_id = "polar-caldron-313623" # enter your project id here
topic_name = "poschairdata" # enter the name of the topic that you created
 
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
 
futures = dict()
 
def get_callback(f, data):
    def callback(f):
        try:
            # print(f.result())
            futures.pop(data)
        except:
            print("Please handle {} for {}.".format(f.exception(), data))
 
    return callback
 
while True:
    time.sleep(3)
    ch0_value = round(main2.poschair()[0],2)
    ch0_voltage = round(float(main2.poschair()[1]),2)
    ch1_value = round(main2.poschair()[2],2)
    ch1_voltage = round(float(main2.poschair()[3]),2)
    ch2_value = round(main2.poschair()[4],2)
    ch2_voltage = round(float(main2.poschair()[5]),2)
    ch3_value = round(main2.poschair()[6],2)
    ch3_voltage = round(float(main2.poschair()[7]),2)
    ch4_value = round(main2.poschair()[8],2)
    ch4_voltage = round(float(main2.poschair()[9]),2)
    ch5_value = round(main2.poschair()[10],2)
    ch5_voltage = round(float(main2.poschair()[11]),2)
    timenow = float(time.time())
    # timenow = datetime.datetime.now()
    data = {"timestamp":timenow, "ch0_value":ch0_value, "ch0_voltage":ch0_voltage,
            "ch1_value":ch1_value, "ch1_voltage":ch1_voltage,
            "ch2_value":ch2_value, "ch2_voltage":ch2_voltage,
            "ch3_value":ch3_value, "ch3_voltage":ch3_voltage,
            "ch4_value":ch4_value, "ch4_voltage":ch4_voltage,
            "ch5_value":ch5_value, "ch5_voltage":ch5_voltage}
    print(data)
    # When you publish a message, the client returns a future.
    future = publisher.publish(
        topic_path, data=(json.dumps(data)).encode("utf-8")) # data must be a bytestring.
    # Publish failures shall be handled in the callback function.
    future.add_done_callback(get_callback(future, data))
    time.sleep(5)
# Wait for all the publish futures to resolve before exiting.
while futures:
    time.sleep(5)
 
print("Published message with error handler.")
