from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Direction(Base):
    __tablename__ = 'directions'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    ideas = relationship('Idea', back_populates='direction')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
    

class Idea(Base):
    __tablename__ = 'ideas'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    direction_id = Column(Integer, ForeignKey('directions.id'))
    direction = relationship('Direction', back_populates='ideas')
    created_at = Column(DateTime(timezone=True), default=datetime.now, server_default=func.now())
