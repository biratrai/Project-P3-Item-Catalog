from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments

# Bind the engine to the base class, makes connections b/w our class definitions and their corresponding tables within our DB
engine = create_engine('sqlite:///project.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()


def get_user_from_username(username):
    """Get user object from given username."""
    return session.query(ProjectName).filter_by(name=name).first()

