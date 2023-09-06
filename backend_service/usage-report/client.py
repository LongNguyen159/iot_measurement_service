
import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime


def simulate_temperature():
    base_temp = 25  
    temp_variation = random.uniform(-3, 3) 
    simulated_temp = base_temp + temp_variation
    return simulated_temp
    

broker_address = "192.168.188.27"
broker_port = 1883
topic = "temperature"

client = mqtt.Client()
client.connect(broker_address, broker_port, 60)

client.loop_start()

try:
    while True:
        deviceID = "1130"
        temperature = simulate_temperature()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature_with_timestamp = f"{deviceID}_{timestamp}_{temperature:.2f}"
        
        print(f"{deviceID}: {temperature:.2f}")
        # client.publish(topic, deviceID)
        client.publish(topic, temperature_with_timestamp)
        time.sleep (2)
except KeyboardInterrupt:
    print("\nProgram terminated")
    client.loop_stop()
    client.disconnect()





