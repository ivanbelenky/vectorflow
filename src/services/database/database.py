import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
database_name = os.getenv('POSTGRES_DATABASE_NAME')
host = os.getenv('POSTGRES_HOST')

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:5432/{database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()