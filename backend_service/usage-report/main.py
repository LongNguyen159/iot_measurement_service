from typing import Union

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


@app.get("/")
async def hello_world():
    return {"Hello": "World"}

@app.get("/drivers")
async def read_all_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    all_drivers = crud.get_all_drivers(db, skip=skip, limit=limit)
    return all_drivers


@app.get("/drivers/{driverId}", response_model=schemas.Driver)
async def read_driver(driverId: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver(db, driver_id= driverId)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver

@app.get("/result/{driverId}")
async def read_driver_records(driverId: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = crud.get_driver_result(db, driver_id=driverId,  skip = skip, limit = limit)
    return [
        {
            "driver_id": record.driver.driverId,
            "driver_name": record.driver.forename + " " + record.driver.surname,
            "driver_code": record.driver.code,
            "race": record.race.name,
            "year": record.race.year,
            "points": record.points
        }
        for record in records
    ]

@app.get("/results")
async def read_yearly_results(year: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    season_results = crud.get_all_results(db, year= year, skip=skip, limit=limit)
    race_names = set(result.race.name for result in season_results)
    driver_points = {}
    
    for result in season_results:
        driver_name = result.driver.forename + " " + result.driver.surname
        race_name = result.race.name
        points = result.points
        
        if driver_name not in driver_points:
            driver_points[driver_name] = {race: 0 for race in race_names}
        
        driver_points[driver_name][race_name] = points
    
    data_for_plot = [
        {"driver": driver, "points": list(points.values())}
        for driver, points in driver_points.items()
    ]
    
    return {"race_names": list(race_names), "data": data_for_plot}
    # return [
    #     {
    #         "result_id": result.driverStandingsId,
    #         "driver_id": result.driver.driverId,
    #         "driver_name": result.driver.forename + " " + result.driver.surname,
    #         "driver_code": result.driver.code,
    #         "race": result.race.name,
    #         "year": result.race.year,
    #         "points": result.points,
    #     }
    #     for result in all_results
    # ]
