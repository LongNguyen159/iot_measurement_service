from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc
from sqlalchemy import func, extract
from sqlalchemy.sql import text
from typing import List
from datetime import datetime, date

import models, schemas

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

def read_results_device(db: Session, ID: int):
    device = db.query(models.Results).filter(
        models.Results.DeviceID == ID).all()
    return device

