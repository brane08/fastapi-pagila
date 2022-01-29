from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from sql.database import Base


class Actor(Base):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True, index=True, name="actor_id")
    first_name = Column(String, unique=True, index=True, name="first_name")
    last_name = Column(String, name="last_name")
    last_update = Column(DateTime, default=True, name="last_update")
