from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc
from sqlalchemy import func, extract
from sqlalchemy.sql import text
from typing import List
from datetime import datetime, date

import models, schemas


# ________old database region________
# def get_driver(db: Session, driver_id: int):
#     return db.query(models.Driver).filter(models.Driver.driverId == driver_id).first()

# def get_all_drivers(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Driver).offset(skip).limit(limit).all()

# # def get_driver_result(db: Session, driver_id: int):
# #     return db.query(models.Results).filter(models.Results.driverId == driver_id)

# def get_all_results(db: Session, year: int, skip: int = 0, limit: int = 100):
#     return db.query(models.Results).join(models.Race).filter(models.Race.year == year).offset(skip).limit(limit).all()


# def get_driver_result(db: Session, driver_id: int, skip: int = 0, limit: int = 100):
#     return db.query(models.Results).filter(models.Results.driverId == driver_id).offset(skip).limit(limit).all()

# def get_years_value(db: Session):
#     return db.query(models.Race.year).distinct().order_by(desc(models.Race.year)).all()
# ________end region________


def read_all_devices(db: Session):
    return db.query(models.Device).all()

def read_all_results(db: Session):
    return db.query(models.Results).all()

def read_daily_results(db: Session, target_date: date):
    results = db.query(models.Results).filter(
        extract('year', models.Results.Timestamp) == target_date.year,
        extract('month', models.Results.Timestamp) == target_date.month,
        extract('day', models.Results.Timestamp) == target_date.day,
    ).all()

    return results

# def read_monthly_results(db: Session)