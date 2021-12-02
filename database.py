from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Setting env variables
load_dotenv()

DB_HOST=os.environ['POSTGRES_HOST']
DB_USER=os.environ['POSTGRES_USER']
DB_PASS=os.environ['POSTGRES_PASSWORD']
DB_NAME=os.environ['POSTGRES_DB']

DB_URL=f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine=create_engine(DB_URL, echo=True)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)