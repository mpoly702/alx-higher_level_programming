from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Create the engine to connect to the database
DATABASE_URL = 'mysql+pymysql://root:Billz@2455@107.23.139.92/TEST_A'
engine = create_engine(DATABASE_URL)

#create a configured "Session" class
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create a base class for our models
Base = declarative_base

# Dependency
def getdb():
    db = Session()
    try:
        yield db
    finally:
        db.close()
