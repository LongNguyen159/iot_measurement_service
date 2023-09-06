from pydantic import BaseModel
from datetime import datetime

# ________old database region________
# class DriverBase(BaseModel):
#     forename: str
#     surname: str
#     code: str
#     nationality: str

# class DriverCreate(DriverBase):
#     pass 

# class Driver(DriverBase):
#     driverId: int
#     class Config:
#         orm_mode = True



# class ResultBase(BaseModel):
#     points: int

# class ResultCreate(ResultBase):
#     pass

# class Result(ResultBase):
#     driverId: int
#     class Config:
#         orm_mode = True

# ________end region________



class Device(BaseModel):
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