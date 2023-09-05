import paho.mqtt.client as mqtt
import time
import sqlite3
import json

def on_connect (client, userdata, flags, rc):
    # client.subscribe(discocovery_topic)
    client.subscribe("temperature")

devices = {}

def on_message (client, userdata, msg):
   
    client_data = (msg.payload.decode())        # decode payload as a string
   

    process_data  = client_data.split("_")
    deviceID = process_data[0]
    timestamp = process_data[1]
    temperature = process_data[2]
    
    print(f"{timestamp}  {temperature}")

    time.sleep(2)

    conn = sqlite3.connect ('temperature_db.sqlite')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Resource (DeviceID, Timestamp, Temperature) VALUES (?, ?, ?)', (deviceID, timestamp, temperature))
    # cursor.execute('INSERT INTO Sensors (DeviceID) VALUES (?)', (deviceID,))
    conn.commit()

    conn.close()

broker_address = "192.168.188.27"
broker_port = 1883
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)

client.loop_start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("\nProgram terminated.")
    client.loop_stop()
    client.disconnect()
   
    