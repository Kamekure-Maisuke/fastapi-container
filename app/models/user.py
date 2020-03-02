# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base
from database import ENGINE

class UserTable(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, autoincrement=True,index=True)
  name = Column(String(128), unique=True, index=True, nullable=False)
  email = Column(String(254), unique=True, index=True, nullable=False)
  password = Column(String(128))
  is_active = Column(Boolean, default=True)

class User(BaseModel):
  id: int
  name: str
  email: str
  password: str
  is_active: bool


def main():
  Base.metadata.create_all(bind=ENGINE)
