import os
import sys

# import sqlalchemy dependencies
from sqlalchemy import Column, ForeignKey, Integer, String
# Declarative allows Table, mapper(), and class objects, which is used to define a mapped class, to be expressed at once within the class declaration.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Returns an instance of new base class of declarative_base from which all mapped classes should inherit
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class MenuItem(Base):
    __tablename__ = 'menu_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant) 

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }    
 
# create_engine function let's us know which database to communicate to
engine = create_engine('sqlite:///restaurantmenu.db')

# Binding the engine and baseclass. This command makes communication between the corresponding tables and class definition
Base.metadata.create_all(engine)