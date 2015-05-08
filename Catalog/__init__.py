# Import Flask class 
from flask import Flask, url_for, render_template 

# Create an instance of Flask ClassBase.metadata.tables.keys() with the name of the 
# running application as the argument any time we run an application in python
app = Flask(__name__)

import Catalog.route
#import Catalog.sqlite
#print app
#print __name__
#print Catalog.route
