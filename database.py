from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

DATABASE_ENDPOINT = "mysql+mysqlconnector://root:@localhost/pdm_62"

db_engine = create_engine(DATABASE_ENDPOINT)
SessionLocal = sessionmaker(autoflush=True, autocommit=False, bind=db_engine)
Base = declarative_base()
