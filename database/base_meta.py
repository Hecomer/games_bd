from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///../games3.db", echo=True)
get_session = sessionmaker(engine, autocommit=False)

