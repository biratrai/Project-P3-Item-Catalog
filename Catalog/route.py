# Imports for Flask
from flask import Flask,render_template, url_for, redirect, flash, request, jsonify 
from Catalog import app
from datetime import datetime

# Imports for DB Session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments

#Imports for using OAuth
from flask import session as login_session
import random, string
import os
from flask import send_from_directory

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

# Imports for XML EndPoints
from xml_helper import create_xml
from flask import Response

# Imports for File Uploads
from werkzeug import secure_filename
from flask import send_from_directory
UPLOAD_FOLDER = 'Catalog/images/'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','JPG'])
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','JPG'])

CLIENT_ID = json.loads(
  open('Catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME= "Restaurant Menu Application"

engine = create_engine('sqlite:///Catalog/project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Project Variables
project_name = ['FullStack','Frontend','ios','Android','Others']
project_fullstack = ['Movie Trailer Website','Tournament Results','Item Catalog','Conference Organization App','Linux Server Configuration']
project_frontend = ['PROJECT P1: Build a Portfolio Site','PROJECT P2: Interactive Resume','PROJECT P3: Classic Arcade Game Clone',
	'PROJECT P4: Website Optimization','PROJECT P5: Neighborhood Map','PROJECT P6: Feed Reader Testing','Additional Projects']
project_ios = ['PROJECT P1: Pitch Perfect','PROJECT P2: MemeMe','PROJECT P3: On the Map','PROJECT P4: Virtual Tourist','Additional Projects']
project_android = ['P1', 'P2']	
project_other = ['O1', 'O2']
projects = ["Project1","Project2","Project3","Project4","Project5"]	
projects_description  = {"Project1":"This is the project one","Project2":"This is the prject 2","Project3":"This is project 3",
			"Project4": "This is project 4","Project5":"This is the project 5"}

#Create anti-forgery state token
@app.route('/login')
def showLogin():
  state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
  login_session['state'] = state
  return render_template('login.html', STATE = state)

@app.route('/gconnect', methods=['POST'])
def gconnect():

#Validate state token 
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

#Obtain authorization code
  code = request.data

  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('Catalog/client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)

# Throw the Error if the authorization code fails
  except FlowExchangeError:
    response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

# Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'% access_token)
  h = httplib2.Http()
  result = json.loads(h.request(url, 'GET')[1])

# If there was an error in the access token info, abort.
  if result.get('error') is not None:
    response = make_response(json.dumps(result.get('error')), 500)
    response.headers['Content-Type'] = 'application/json'

# Verify that the access token is used for the intended user.
  gplus_id = credentials.id_token['sub']
  if result['user_id'] != gplus_id:
    response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

# Verify that the access token is valid for this app.
  if result['issued_to'] != CLIENT_ID:
    response = make_response(json.dumps("Token's client ID does not match app's."), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

#Check to see if user is already logged in
  stored_credentials = login_session.get('credentials')
  stored_gplus_id = login_session.get('gplus_id')
  if stored_credentials is not None and gplus_id == stored_gplus_id:
    response = make_response(json.dumps('Current user is already connected.'),200)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Store the access token in the session for later use.
  login_session['credentials'] = credentials
  login_session['gplus_id'] = gplus_id

  #Get user info
  userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt':'json'}
  answer = requests.get(userinfo_url, params=params)

  data = answer.json()
  login_session['provider'] = 'google'
  login_session['username'] = data['name']
  login_session['picture'] = data['picture']
  login_session['email'] = data['email']

  # see if user exists
  user_id = getUserID(login_session['email'])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id
  print login_session['user_id']

  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("You are now logged in as %s"%login_session['username'])
  return output

#Revoke current user's token and reset their login_session.
@app.route("/gdisconnect")
def gdisconnect():
  
  # Only disconnect a connected user.
  credentials = login_session.get('credentials')
  if credentials is None:
    response = make_response(json.dumps('Current user not connected.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Execute HTTP GET request to revoke current token.
  access_token = credentials.access_token
  url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]

  if result['status'] == '200':
    # Reset the user's session.
    response = make_response(json.dumps('Successfully disconnected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
  else:
    # For whatever reason, the given token was invalid.
    response = make_response(
        json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response
  access_token = request.data

  #Exchange client token for long-lived server-side token
  # GET /oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token} 
  app_id = json.loads(open('Catalog/fb_client_secrets.json', 'r').read())['web']['app_id']
  app_secret = json.loads(open('Catalog/fb_client_secrets.json', 'r').read())['web']['app_secret']
  url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id,app_secret,access_token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]

  #Use token to get user info from API 
  userinfo_url =  "https://graph.facebook.com/v2.2/me"

  #strip expire tag from access token
  token = result.split("&")[0]

  url = 'https://graph.facebook.com/v2.2/me?%s' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  print "result\n",result

  data = json.loads(result)
  print "\ndata\n",type(data),data
  login_session['provider'] = 'facebook'
  login_session['username'] = data["name"]
  login_session['email'] = data["name"]+"@facebook.com"
  login_session['facebook_id'] = data["id"]

  # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
  stored_token = token.split("=")[1]
  login_session['access_token'] = stored_token

  #Get user picture
  url = 'https://graph.facebook.com/v2.2/me/picture?%s&redirect=0&height=200&width=200' % token
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  data = json.loads(result)

  login_session['picture'] = data["data"]["url"]
	  
	# see if user exists
  user_id = getUserID(login_session['email'])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id

  output = ''
  output +='<h1>Welcome, '
  output += login_session['username']

  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output +=' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

  flash ("Now logged in as %s" % login_session['username'])
  return output

@app.route('/fbdisconnect')
def fbdisconnect():
  facebook_id = login_session['facebook_id']

  # The access token must me included to successfully logout
  access_token = login_session['access_token']
  url = 'https://graph.facebook.com/%s/permissions' % (facebook_id,access_token)
  h = httplib2.Http()
  result = h.request(url, 'DELETE')[1]
  return "you have been logged out"


@app.route('/disconnect')
def disconnect():
  if 'provider' in login_session:
    if login_session['provider'] == 'google':
      gdisconnect()
      del login_session['gplus_id']
      del login_session['credentials']
    if login_session['provider'] == 'facebook':
      fbdisconnect()
      del login_session['facebook_id']

    del login_session['username']
    del login_session['email']
    del login_session['picture']
    del login_session['provider']
    flash("You have successfully been logged out.")
    return redirect(url_for('index'))
  else:
    flash("You were not logged in")
    return redirect(url_for('index'))

# Route for HomePage 
@app.route('/')
@app.route('/index')
def index():
	if 'username' not in login_session:
		return render_template("public_index.html",title='Home')
	else:
		return render_template("index.html",title='Home')
	
# Route for favicon request
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/default')
def default_jsonencoder():
  now = str(datetime.now())
  return json.dumps({'now': now})

# Route for Project Page 
@app.route('/<project>/')
def projectMain(project):
  if((str(project)) == 'fullstack'):
    project_category = project_fullstack
  elif((str(project)) == 'frontend'):
    project_category = project_frontend
  elif((str(project)) == 'ios'):
    project_category = project_ios
  elif((str(project)) == 'android'):
    project_category = project_android
  elif((str(project)) == 'others'):
    project_category = project_other
  else:
    return "Wrong path"
  
  return render_template('project.html',project_category = project_category,project=str(project))  

#JSON APIs to view Project Information
@app.route('/<project>/<projectcategory>/JSON')
def projectCategoryJSON(project,projectcategory):
  project_list = session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()
  return jsonify(Projects=[i.serialize for i in project_list])

#XML APIs to view Project Information
@app.route('/<project>/<projectcategory>/XML')
def projectCategoryJSON(project,projectcategory):
  project_list = session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()
  return Response(create_xml(project,projectcategory,project_list), mimetype='application/xml')

# Route for Project Category Page
@app.route('/<project>/<projectcategory>/')
def projectCategory(project,projectcategory):
  
  project_query = session.query(Project).filter_by(projectname_id = project, projectcategory_id=projectcategory).all();
  
  return render_template('projectcategory.html',project_name = projects,project=str(project),
		projectcategory=str(projectcategory),project_list=project_query) 	

# Route for displaying project
@app.route('/<project>/<projectcategory>/<int:project_no>/',methods=['GET', 'POST'])       
def showProject(project,projectcategory,project_no):
  project_no_query = session.query(Project).filter_by(project_item_id = project_no).one()
  creator = getUserInfo(project_no_query.author_id)
  author_name = getUserName(project_no_query.author_id)
  
  project_comment_query = session.query(Comments,User).filter(Comments.author_id == User.id).\
    filter(Comments.project_id == project_no).all()    
  
  # Check to see if user in logged in or not
  if 'username' not in login_session:
    return redirect('/login')
  
  # Handle the POST request  
  if request.method == 'POST':
    print request.form['comments']
    newComment = Comments(content = request.form['comments'],author_id=login_session['user_id'],project_id=project_no)
    session.add(newComment)
    session.commit()

  if 'username' not in login_session or creator.id != login_session['user_id']:
    return render_template('public_single_project.html',project=project,projectcategory=projectcategory,project_no=project_no,
      project_list=project_no_query, author_name=author_name,project_comments = project_comment_query)
  else:
    return render_template('single_project.html', project=project,projectcategory=projectcategory,project_no=project_no,
      project_list=project_no_query, author_name=author_name,project_comments = project_comment_query)

# Route for editing project
@app.route('/<project>/<projectcategory>/<int:project_no>/edit/',methods=['GET', 'POST'])
def editProject(project,projectcategory,project_no):
  editedProject = session.query(Project).filter_by(project_item_id = project_no).one()

  if editedProject.author_id != login_session['user_id']:
    return "<script>function myFunction() {alert('You are not authorized to edit this project. Please create your own project in order to edit.');}</script><body onload='myFunction()''>"
  
  if 'username' not in login_session:
    return redirect('/login')

  if request.method == 'POST':
    if request.form['name']:
      editedProject.project_url = request.form['name']
      editedProject.project_description = request.form['description']
      flash('New Project %s Successfully Created' % editedProject.project_url)
      return redirect(url_for('projectCategory',project=project,projectcategory=projectcategory))
  else:
    return render_template('edit_project.html',project = project,projectcategory=projectcategory,
    project_no=project_no,project_url=editedProject.project_url,project_description=editedProject.project_description)

# Route for deleting project
@app.route('/<project>/<projectcategory>/<int:project_no>/delete/',methods=['GET', 'POST'])
def deleteProject(project,projectcategory,project_no):
  projectToDelete = session.query(Project).filter_by(project_item_id = project_no).one()

  # Check to see if user in logged in or not
  if 'username' not in login_session:
    return redirect('/login')
	
  # Alert user if they are authorized to delete the project
  if projectToDelete.author_id != login_session['user_id']:
    return "<script>function myFunction() {alert('You are not authorized to project this project. Please create your own project in order to delete.');}</script><body onload='myFunction()''>"

  if request.method == 'POST':
    session.delete(projectToDelete)
    flash('%s Successfully Deleted' % projectToDelete.project_url)
    session.commit()
    return redirect(url_for('projectCategory',project=project,projectcategory=projectcategory))
  else:
    return render_template('delete_project.html',project = project,projectcategory=projectcategory,project_no=project_no)

# Function to check for the allowed extensions for uploading files
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# Route for creating new Project
@app.route('/<project>/<projectcategory>/new', methods=['GET','POST'])
def newProject(project,projectcategory):

  # Check to see if user in logged in or not
  if 'username' not in login_session:
    return redirect('/login')

  # Handle the POST request  
  if request.method == 'POST':
    # Get the name of the uploaded file
    file = request.files['file']
    print file.filename

    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
      # Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)
      print type(file)

      # Move the file form the temporal folder to the upload folder we setup
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Save data into database  
    newProject = Project(project_url = request.form['url'],
      author_id=login_session['user_id'],
      project_description= request.form['description'],
      projectname_id=project,
      projectcategory_id=projectcategory)
    session.add(newProject)

    # Show flash message about succesfull creation of project
    flash('New Project %s Successfully Created' % newProject.project_url)
    session.commit()
    return redirect(url_for('projectCategory',project=project,projectcategory=projectcategory))
  else:
    return render_template('new_project.html',project = project,projectcategory=projectcategory)

# Function to query user email
def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

# Function to query user id
def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user

# Function to query user id
def getUserName(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return user.name

# Function to Create New User into database
def createUser(login_session):
    newUser = User(name = login_session['username'], email = login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email = login_session['email']).one()
    return user.id   
