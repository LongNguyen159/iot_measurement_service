from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from database import Base

Base = declarative_base()

class Device(Base):
    __tablename__ = "Sensors"
    ID = Column(Integer, primary_key=True)
    # Name = Column(String)
   

    results = relationship("Results", back_populates="device")

class Results(Base):
    __tablename__ = "Resource"
    ID = Column(Integer, primary_key=True)
    Timestamp = Column(String)
    Temperature = Column(Float)
    DeviceID = Column(Integer, ForeignKey('Sensors.ID'))

    device = relationship("Device", back_populates="results")