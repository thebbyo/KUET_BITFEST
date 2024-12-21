
from xmlrpc.client import Boolean
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, BOOLEAN, Text
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta
from sqlalchemy import DateTime

from sqlalchemy.dialects.postgresql import ARRAY

import enum




# Define an Enum for units
class UnitEnum(enum.Enum):
    L = "L"
    KG = "KG"
    GRAM = "GRAM"
    ML = "ML"
    PIECE = "PIECE"

class Ingredients(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    quantity = Column(Integer)
    unit = Column(String, nullable=False, default=UnitEnum.PIECE.value)