import os
import sys

# import sqlalchemy dependencies
from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME, func
from datetime import datetime

# Declarative allows Table, mapper(), and class objects, which is used to define a mapped class, to be expressed at once within the class declaration.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Returns an instance of new base class of declarative_base from which all mapped classes should inherit
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
   
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    email = Column(String(64))
    
class Project(Base):
    __tablename__ = 'projectitems'

    project_item_id = Column(Integer,primary_key = True)
    project_url = Column(String(250), nullable = False)
    project_description = Column(String(250))
    createdTime = Column(DATETIME,default=func.current_timestamp())
    author_id = Column(Integer,ForeignKey('users.id'))
    projectname_id = Column(String(64),nullable = False)
    projectcategory_id =Column(String(64),nullable = False)
    user = relationship(User,cascade = 'delete')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
           'name'           : self.project_url,
           'id'             : self.project_item_id,
           'description'    : self.project_description,
           'created'        : str(self.createdTime),
           'projectname'    : self.projectname_id,
           'projectcategory': self.projectcategory_id,
           'author'         : self.author_id,
        }

class Comments(Base):
    __tablename__ = 'comments'    

    comment_id = Column(Integer,primary_key = True)
    content = Column(String(200),nullable =False)
    createdTime = Column(DATETIME, default=func.current_timestamp())
    author_id = Column(Integer,ForeignKey('users.id'))
    project_id = Column(Integer,ForeignKey('projectitems.project_item_id'))
    user = relationship(User,cascade = 'delete')
    projectitems = relationship(Project,cascade = 'delete')  

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'        : self.comment_id,
            'content'   : self.content,
            'author'    : self.author_id,
            'projectid' : self.project_id,
            'created'   : str(self.createdTime),
        }
      
# create_engine function let's us know which database to communicate to
engine = create_engine('sqlite:///project.db')

# Binding the engine and baseclass. This command makes communication between the corresponding tables and class definition
Base.metadata.create_all(engine)