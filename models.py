from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime as _dt

class Movie(Base):
    __tablename__ = "movies"

    id= Column(Integer, primary_key=True, index=True)
    name= Column(String)
    description= Column(String)
    rating= Column(Integer, default=0)
    playing_date = Column(DateTime, default=_dt.datetime.utcnow)
    created_date = Column(DateTime, default=_dt.datetime.utcnow)
    last_updated = Column(DateTime, default=_dt.datetime.utcnow)