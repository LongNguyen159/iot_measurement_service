from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
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

@app.get('/results')
async def get_all_results(db: Session = Depends(get_db)):
    return crud.read_all_results(db)

@app.get('/daily-results', response_model=List[schemas.Result])
async def get_daily_results(target_date: date, db: Session = Depends(get_db)):
    daily_results = crud.read_daily_results(db, target_date)
    return daily_results


@app.get("/results/serial")
async def read_serial_number(ID: int, db: Session = Depends(get_db)):
    serial = crud.read_results_device(db, ID)
    return serial

# @app.get('/monthly-results')
# async def get_monthly_results(target_month: int, target_year: int, db: Session = Depends(get_db)):
#     monthly_results = crud.read_monthly_results()
#     return monthly_results

