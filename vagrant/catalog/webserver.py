from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# Import CRUD operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/hello"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h1>Hello!</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

			if self.path.endswith("/hola"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ""
				output += "<html><body>"
				output += "<h1>&#161 Hola !</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				print output
				return

			#look for url that ends with '/restaurants'
			if self.path.endswith("/restaurants"):
				self.send_response(200)

				#indicate reply in form of html to the client
				self.send_header('Content-type','text/html')

				#indicates end of https headers in the response
				self.end_headers()

				#obtain all restaurant names from databse
				restaurants = session.query(Restaurant).all()
				#print (restaurants)
				
				output = ""
				output += "<html><body>"
				output += "<a href='/restaurants/new'>Make a new Restaurants here</a>"
				output += "<br></br>"
				for restaurant in restaurants:
					output += restaurant.name
					#print restaurant.id
					output += "<br></br>"
					#output += "<a href={0}>Edit</a>".format(str(restaurant.id)+"/edit")
					output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
					output += "<br></br>"
					#output += "<a href={0}>Delete</a>".format(str(restaurant.id)+"/delete")
					output += "<a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
					output += "<br></br>"
					output += "<br></br>"
					output += "<br></br>"
				output += "</body></html>"
				self.wfile.write(output)	
				#print output
				return

			# look for url that ends with '/new'
			if self.path.endswith("/restaurants/new"):
				self.send_response(200)

				self.send_header('Content-type','text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h1>Make a New Restaurant</h1>"
				output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>"
				output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
				output += "<input type='submit' value='Create'>"
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith("/delete"):
				self.send_response(200)

				self.send_header('Content-type','text/html')
				self.end_headers()

				output = ""
				output += "<html><body>"
				output += "<h1>Are you sure you want to Delete Restaurant</h1>"
				output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><input type="submit" value="Delete"> </form>'''
				output += "</body></html>"
				self.wfile.write(output)
				return

			if self.path.endswith("/edit"):
				restaurantIDPath = self.path.split("/")[2]
				print restaurantIDPath, self.path
				print session.query(Restaurant)
				myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
				print myRestaurantQuery

				if myRestaurantQuery:
					self.send_response(200)

					self.send_header('Content-type','text/html')
					self.end_headers()

					output = ""
					output += "<html><body>"
					output += "<h1>Edit Restaurant</h1>"
					output += '''<form method='POST' enctype='multipart/form-data' action='/hola'><input name="message" type="text" ><input type="submit" value="Edit"> </form>'''
					output += "</body></html>"
					self.wfile.write(output)

		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)


	def do_POST(self):
		try:
			if self.path.endswith("/restaurants/new"):
				# Parse a MIME header (such as Content-Type) into a main value(ctype) and a dictionary(pdict) of parameters.
				print "self.headers",type(self.headers),self.headers
				print "content-type",self.headers.getheader('content-type')
				ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
				print ctype
			
				if ctype == 'multipart/form-data':
					# Parses the input of type multipart/form-data (for file uploads)into dictionary with key as message and value as the field from the form
					fields = cgi.parse_multipart(self.rfile,pdict)
					print type(self.rfile),self.rfile,pdict,fields
					messagecontent = fields.get('newRestaurantName')

					#Create new Restaurant Object
					newRestaurant = Restaurant(name = messagecontent[0])
					session.add(newRestaurant)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location','/restaurants')
					self.end_headers()
				#print output
		except:
			pass


def main():
	try:
		port = 8000
		server = HTTPServer(('', port), webServerHandler)
		print "Web Server running on port %s"  % port
		server.serve_forever()
	except KeyboardInterrupt:
		print " ^C entered, stopping web server...."
		server.socket.close()

if __name__ == '__main__':
	main()