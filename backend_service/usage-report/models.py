from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Driver(Base):
    __tablename__ = "drivers"
    driverId = Column(Integer, primary_key=True)
    forename = Column(String(30))
    surname = Column(String(30))
    code = Column(String(10))
    nationality = Column(String)
    results = relationship("Results", back_populates="driver")

class Race(Base):
    __tablename__ = "races"
    raceId = Column(Integer, primary_key=True)
    year = Column(Integer)
    name = Column(String)
    results = relationship("Results", back_populates="race")

class Results(Base):
    __tablename__ = "driver_standings"
    driverStandingsId = Column(Integer, primary_key=True)
    driverId = Column(Integer, ForeignKey('drivers.driverId'))
    raceId = Column(Integer, ForeignKey('races.raceId'))
    points = Column(Integer)
    
    driver = relationship("Driver", back_populates="results", lazy="joined")
    race = relationship("Race", back_populates="results", lazy="joined")


