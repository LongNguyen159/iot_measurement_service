import paho.mqtt.client as mqtt
import time
import json
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Results, Device
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
   
def on_connect (client, userdata, flags, rc):
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

    DATABASE_URL = "sqlite:///temperature_db.sqlite"

    engine = create_engine(DATABASE_URL)
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    temperature_reading = Results()
    temperature_reading.DeviceID = deviceID
    temperature_reading.Timestamp = timestamp
    temperature_reading.Temperature = temperature

    session.add(temperature_reading)
    session.commit()
    session.rollback()
        
    session.close()

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
   

    
