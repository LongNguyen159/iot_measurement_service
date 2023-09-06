from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fastapi.middleware.cors import CORSMiddleware
from datetime import date, datetime

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get('/devices')
async def get_all_devices(db: Session = Depends(get_db)):
    return crud.read_all_devices(db)

@app.get('/results', response_model=List[schemas.Result])
async def get_all_results(db: Session = Depends(get_db)):
    return crud.read_all_results(db)

@app.get('/daily-results', response_model=List[schemas.Result])
async def get_daily_results(target_date: date, db: Session = Depends(get_db)):
    daily_results = crud.read_daily_results(db, target_date)
    return daily_results

# @app.get('/monthly-results')
# async def get_monthly_results(target_month: int, target_year: int, db: Session = Depends(get_db)):
#     monthly_results = crud.read_monthly_results()
#     return monthly_results



# ________old database region________

# @app.get("/years/")
# async def read_years_value(db: Session = Depends(get_db)):
#     return crud.get_years_value(db)

# @app.get("/drivers")
# async def read_all_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     all_drivers = crud.get_all_drivers(db, skip=skip, limit=limit)
#     return all_drivers


# @app.get("/drivers/{driverId}", response_model=schemas.Driver)
# async def read_driver(driverId: int, db: Session = Depends(get_db)):
#     db_driver = crud.get_driver(db, driver_id= driverId)
#     if db_driver is None:
#         raise HTTPException(status_code=404, detail="Driver not found")
#     return db_driver

# @app.get("/result/{driverId}")
# async def read_driver_records(driverId: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     records = crud.get_driver_result(db, driver_id=driverId,  skip = skip, limit = limit)
#     return [
#         {
#             "driver_id": record.driver.driverId,
#             "driver_name": record.driver.forename + " " + record.driver.surname,
#             "driver_code": record.driver.code,
#             "race": record.race.name,
#             "year": record.race.year,
#             "points": record.points
#         }
#         for record in records
#     ]

# @app.get("/results/{year}")
# async def read_yearly_results(year: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     season_results = crud.get_all_results(db, year= year, skip=skip, limit=limit)
#     race_names = set(result.race.name for result in season_results)
#     driver_points = {}
    
#     for result in season_results:
#         driver_name = result.driver.forename + " " + result.driver.surname
#         race_name = result.race.name
#         points = result.points
        
#         if driver_name not in driver_points:
#             driver_points[driver_name] = {race: 0 for race in race_names}
        
#         driver_points[driver_name][race_name] = points
    
#     data_for_plot = [
#         {"driver": driver, "points": list(points.values())}
#         for driver, points in driver_points.items()
#     ]
    
#     return {"race_names": list(race_names), "data": data_for_plot}



# @app.get("/plot-yearly-results/{year}")
# async def plot_yearly_results(year: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     yearly_data = await read_yearly_results(year, skip, limit, db)
    
#     fig = make_subplots(specs=[[{"secondary_y": True}]])
    
#     for driver_data in yearly_data["data"]:
#         fig.add_trace(
#             go.Scatter(x=yearly_data["race_names"], y=driver_data["points"], mode="lines", name=driver_data["driver"]),
#             secondary_y=False,
#         )
    
#     fig.update_layout(
#         title=f"Driver Points in {year}",
#         xaxis_title="Races",
#         yaxis_title="Points",
#     )
    
#     return fig.show()

# ________end region________