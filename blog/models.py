from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    bio = Column(String(500))
    email = Column(String(30),unique=True)
    password = Column(String(100))
    companyname = Column(String(50))
    website = Column(String(50))
    address = Column(String(100))
    country = Column(String(50))
    state = Column(String(50))
    city = Column(String(100))
    zipcode = Column(String(11))
