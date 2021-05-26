from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from model import db

class Anode(db.Base):
    __tablename__ = 'anode'

    id = Column(Integer, primary_key=True)
    origin = Column(String)
    component = Column(String)
    model = Column(String)
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    d = Column(Float)
    e = Column(Integer)
    description = Column(String)
    manuforiented = Column(Boolean)
    label = Column(String)

class Cathode(db.Base):
    __tablename__ = 'cathode'

    id = Column(Integer, primary_key=True)
    origin = Column(String)
    component = Column(String)
    model = Column(String)
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    d = Column(Float)
    e = Column(Integer)
    description = Column(String)
    manuforiented = Column(Boolean)
    estimation = Column(Boolean)
    label = Column(String)

class Thermal(db.Base):
    __tablename__ = 'thermal'

    id = Column(Integer, primary_key=True)
    origin = Column(String)
    component = Column(String)
    model = Column(String)
    a = Column(Float)
    b = Column(Float)
    c = Column(Float)
    d = Column(Float)
    e = Column(Integer)
    description = Column(String)
    manuforiented = Column(Boolean)
    estimation = Column(Boolean)
    label = Column(String)



