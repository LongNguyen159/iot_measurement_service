from pydantic import BaseModel
from datetime import datetime

class Device(BaseModel):
    ID : int
    Name: str

    class Config:
        orm_mode = True

class Result(BaseModel):
    ID: int
    DeviceID: int
    Timestamp: datetime
    Temperature: float

    class Config:
        orm_mode = True