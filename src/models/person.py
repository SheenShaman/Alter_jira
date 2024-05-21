from src.config.db import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # tasks = relationship("Task", back_populates="person")
