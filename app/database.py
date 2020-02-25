# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import MYSQL_URI

ENGINE = create_engine(
  MYSQL_URI,
  encoding="utf-8",
  echo=True
)

session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=ENGINE
  )
)

Base = declarative_base()
Base.query = session.query_property()
