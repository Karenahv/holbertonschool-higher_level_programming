#!/usr/bin/python3
"""class User"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """class state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """return instance"""
        return "{}: {}".format(self.id, self.name)
