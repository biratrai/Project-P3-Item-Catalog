#!flask/bin/python
from app import app


#app.run(debug=True)
 #  run the local server with our application and make the server publicly available
#app.run(host = '0.0.0.0', port = 5000)
if __name__ == '__main__':

  # enable debug support the server will reload itself on code changes
	app.debug = True

  #  run the local server with our application and make the server publicly available
	app.run(host = '0.0.0.0', port = 8000)
