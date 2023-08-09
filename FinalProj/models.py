from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
