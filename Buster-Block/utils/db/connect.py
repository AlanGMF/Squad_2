import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv, find_dotenv

# Load configuration file
load_dotenv(find_dotenv())
USER = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('DATABASE_HOST')
PORT = os.getenv('PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')

# Create connection to the db
engine = sqlalchemy.create_engine("postgresql://" + USER + ":" + PASSWORD +
                                  "@" + HOST + ":" + PORT + "/" +
                                  DATABASE_NAME)
conn = engine.connect()
session = Session(bind=engine)

Base = declarative_base()
