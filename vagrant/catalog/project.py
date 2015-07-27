# -*- coding: utf-8 -*-
# import the Flask class.
from flask import Flask

# create an instance of this class. The first argument is the name of the application’s module or package.
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# decorator is used to bind a function to a URL
@app.route('/') 
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
  # one(), fully fetches all rows, and if not exactly one object identity or composite row is present in the result, raises an error
  restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one() 
  items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
  output = ''
  for i in items:
    output += i.name
    output += '</br>'
    output += i.price
    output += '</br>'
    output += i.description
    output +='</br>'
    output +='</br>'
  return output
  
if __name__ == '__main__':

  # enable debug support the server will reload itself on code changes
	app.debug = True

  #  run the local server with our application and make the server publicly available
	app.run(host = '0.0.0.0', port = 5000)