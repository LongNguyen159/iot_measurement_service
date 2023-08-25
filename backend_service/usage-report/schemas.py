from pydantic import BaseModel

class DriverBase(BaseModel):
    forename: str
    surname: str
    code: str
    nationality: str

class DriverCreate(DriverBase):
    pass 

class Driver(DriverBase):
    driverId: int
    class Config:
        orm_mode = True



class ResultBase(BaseModel):
    points: int

class ResultCreate(ResultBase):
    pass

class Result(ResultBase):
    driverId: int
    class Config:
        orm_mode = True

