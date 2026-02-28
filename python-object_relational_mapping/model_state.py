#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that links to the MySQL table 'cities'.

    Attributes:
        id (int): Auto-generated, unique integer, primary key.
        name (string): String of max 128 characters, cannot be null.
        state_id (int): Foreign key to states.id, cannot be null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
