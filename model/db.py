from psycopg2 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:admin@localhost:5432/InnBalance_reviewered')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()