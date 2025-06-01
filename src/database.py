from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String, Integer, DateTime, Boolean
from datetime import datetime

Base = declarative_base()


class HabitScore(Base):
    "Define the table in the database"
    __tablename__ = "habitscore"

    id = Column(Integer,primary_key=True,autoincrement=True)
    habit = Column(String(50), nullable = False)
    Value = Column(Boolean, nullable = False)
    