from sqlmodel import create_engine, SQLModel, Session, select
import models


sqlite_file_name = 'database.sqlite'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)
