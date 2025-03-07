#!/usr/bin/python3
"""A python file that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """An object representation of the table Cities in our database"""
    __tablename__ = "cities"

    """Primary key makes the attribute unique, non null and autogenerated"""
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
