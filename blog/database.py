from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL ='sqlite:///blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args ={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autocommit=False)
Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#postgres://avnadmin:AVNS_cWkWpaCKpa4B9qks-sE@pg-2d7611d5-blogdevcode-0684.a.aivencloud.com:22660/defaultdb?sslmode=require