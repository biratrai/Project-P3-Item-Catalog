from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

print('Your SQLAlchemy session is ready to go! Access it with `session`')
#print Base.metadata.tables.keys()
print Base.metadata.tables['restaurant']
for user in session.query(MenuItem):
     print user.name