from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    #email = Column(E)
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
