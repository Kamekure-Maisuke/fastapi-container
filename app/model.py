# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

class TaskTable(Base):
  __tablename__ = 'task'
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String(50), nullable=False)

class Task(BaseModel):
  id: int
  title: str


def main():
  Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
  main()
