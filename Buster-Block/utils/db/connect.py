import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv, find_dotenv
import utils.log_control as log_control

log_control.loggerDB.info('Starting database connection')
try:
    # Load configuration file
    load_dotenv(find_dotenv())
    USER = os.getenv('USER')
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
    log_control.loggerDB.info('Successful connection!')

except Exception as e:
    msj = 'Database connection error, info: '
    log_control.loggerDB.error(f'{msj}{e}')

