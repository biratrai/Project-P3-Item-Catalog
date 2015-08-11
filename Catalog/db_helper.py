# Imports for DB Session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments

# Connect to the database
engine = create_engine('sqlite:///Catalog/project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()