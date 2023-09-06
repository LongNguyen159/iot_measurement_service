from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base

# ________old database region________
# class Driver(Base):
#     __tablename__ = "drivers"
#     driverId = Column(Integer, primary_key=True)
#     forename = Column(String(30))
#     surname = Column(String(30))
#     code = Column(String(10))
#     nationality = Column(String)
#     results = relationship("Results", back_populates="driver")

# class Race(Base):
#     __tablename__ = "races"
#     raceId = Column(Integer, primary_key=True)
#     year = Column(Integer)
#     name = Column(String)
#     results = relationship("Results", back_populates="race")

# class Results(Base):
#     __tablename__ = "driver_standings"
#     driverStandingsId = Column(Integer, primary_key=True)
#     driverId = Column(Integer, ForeignKey('drivers.driverId'))
#     raceId = Column(Integer, ForeignKey('races.raceId'))
#     points = Column(Integer)
    
#     driver = relationship("Driver", back_populates="results", lazy="joined")
#     race = relationship("Race", back_populates="results", lazy="joined")

# ________end region________

class Device(Base):
    __tablename__ = "Sensors"
    ID = Column(Integer, primary_key=True)
    Name = Column(String)

    results = relationship("Results", back_populates="device")

class Results(Base):
    __tablename__ = "Resource"
    ID = Column(Integer, primary_key=True)
    Timestamp = Column(DateTime)
    Temperature = Column(Float)
    DeviceID = Column(Integer, ForeignKey('Sensors.ID'))

    device = relationship("Device", back_populates="results", lazy='joined')