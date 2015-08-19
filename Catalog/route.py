# Imports for Flask
from flask import Flask, render_template, url_for
from flask import redirect, flash, request, jsonify
from Catalog import app
from datetime import datetime

# Imports for DB Session
import db_helper

# Import for Login Decorator
from functools import wraps
from flask import g, request

# Imports for using OAuth
from flask import session as login_session
import random
import string
import os
from flask import send_from_directory

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response

# SeaSurf is a Flask Extension for preventing cross-site request forgery
from flask.ext.seasurf import SeaSurf

# import requests
import social_login_helper

# Imports for XML EndPoints
from xml_helper import create_xml
from flask import Response

# Imports for File Uploads
from werkzeug import secure_filename
from flask import send_from_directory
UPLOAD_FOLDER = 'Catalog/static/'

# Allowed extensions for the image
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPG'])
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'JPG'])

# Protecting the app against CSRF attacks.
csrf = SeaSurf(app)

CLIENT_ID = json.loads(
  open('Catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"

# Project Variables
project_fullstack = ['Movie Trailer Website', 'Tournament Results',
'Item Catalog', 'Conference Organization App', 'Linux Server Configuration']
project_frontend = ['PROJECT P1: Build a Portfolio Site',
'PROJECT P2: Interactive Resume',
'PROJECT P3: Classic Arcade Game Clone',
'PROJECT P4: Website Optimization', 'PROJECT P5: Neighborhood Map',
'PROJECT P6: Feed Reader Testing', 'Additional Projects']
project_ios = ['PROJECT P1: Pitch Perfect', 'PROJECT P2: MemeMe',
'PROJECT P3: On the Map', 'PROJECT P4: Virtual Tourist', 'Additional Projects']
project_android = ['P1', 'P2']	
project_other = ['O1', 'O2']
projects = ["Project1", "Project2", "Project3", "Project4", "Project5"]	

@app.route('/login')
def showLogin():
  ''' Create anti-forgery state token '''
  state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
  login_session['state'] = state
  return render_template('login.html', STATE = state)

# Connect to Gmail and store credentials and fields
@csrf.exempt
@app.route('/gconnect', methods=['POST'])
def gconnect():
  output = social_login_helper.google_connect(request,login_session)
  return output

#Revoke Gmail user's token and reset their login_session.
@app.route("/gdisconnect")
def gdisconnect():
  social_login_helper.google_disconnect(login_session)

# Connect to Fbook and store credentials and fields
@csrf.exempt
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
  output = social_login_helper.fb_connect(request,login_session)
  return output

#Revoke Fbook user's token and reset their login_session.
@app.route('/fbdisconnect')
def fbdisconnect():
  output = social_login_helper.fb_disconnect(login_session)
  return output

# Route for logging out
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
  # project_list = session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()
  project_list = db_helper.jsonRequest()
  return jsonify(Projects=[i.serialize for i in project_list])

#XML APIs to view Project Information
@app.route('/<project>/<projectcategory>/XML')
def projectCategoryXML(project,projectcategory):
  # project_list = session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()
  project_list = db_helper.jsonRequest()
  return Response(create_xml(project,projectcategory,project_list), mimetype='application/xml')

# Route for Project Category Page
@app.route('/<project>/<projectcategory>/')
def projectCategory(project,projectcategory):
  list_of_projects = db_helper.project_list(project,projectcategory)
  
  return render_template('projectcategory.html',project_name = projects,project=str(project),
		projectcategory=str(projectcategory),project_list=list_of_projects) 	

# Route for displaying project
@app.route('/<project>/<projectcategory>/<int:project_no>/',methods=['GET', 'POST'])       
def showProject(project,projectcategory,project_no):
  list_of_single_project = db_helper.single_project(project_no)
  creator = db_helper.getUserInfo(list_of_single_project.author_id)
  author_name = db_helper.getUserName(list_of_single_project.author_id)
     
  list_of_comments = db_helper.comments_list(project_no)  
  
  # Handle the POST request  
  if request.method == 'POST':
    if 'username' not in login_session:
          return redirect('/login')
    else:
      newComment = db_helper.new_comments(request.form['comments'],login_session['user_id'],project_no)
      return render_template('single_project.html', project=project,projectcategory=projectcategory,project_no=project_no,
      project_list=list_of_single_project, author_name=author_name,project_comments = list_of_comments)

  if 'username' not in login_session or creator.id != login_session['user_id']:
    return render_template('public_single_project.html',project=project,projectcategory=projectcategory,project_no=project_no,
      project_list=list_of_single_project, author_name=author_name,project_comments = list_of_comments)
  else:
    return render_template('single_project.html', project=project,projectcategory=projectcategory,project_no=project_no,
      project_list=list_of_single_project, author_name=author_name,project_comments = list_of_comments)

# @app.route('/<path:filename>')  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

# View Decorator for login check
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
          return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

# Route for editing project
@app.route('/<project>/<projectcategory>/<int:project_no>/edit/',methods=['GET', 'POST'])
@login_required
def editProject(project,projectcategory,project_no):
  
  editedProject = db_helper.edit_project(project_no)

  if editedProject.author_id != login_session['user_id']:
    return "<script>function myFunction() {alert('You are not authorized to edit this project. Please create your own project in order to edit.');}</script><body onload='myFunction()''>"
  
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
@login_required
def deleteProject(project,projectcategory,project_no):
  
  projectToDelete = db_helper.delete_project(project_no)

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
@login_required
def newProject(project,projectcategory):

  # Handle the POST request  
  if request.method == 'POST':
    # Get the name of the uploaded file
    file = request.files['file']

    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
      # Make the filename safe, remove unsupported chars
      filename = secure_filename(file.filename)

      # Move the file form the temporal folder to the upload folder we setup
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

      # Get image path
      image_url = url_for('static',filename=file.filename)

    # Save data into database  
    newProject = db_helper.new_project(request.form['url'],
      login_session['user_id'],request.form['description'],project,projectcategory,image_url)

    # Create and Save new User into database
    newUser = db_helper.new_user(login_session['username'],login_session['user_id'])

    # Show flash message about succesfull creation of project
    flash('New Project %s Successfully Created' % newProject.project_url)
    # session.commit()
    return redirect(url_for('projectCategory',project=project,projectcategory=projectcategory))
  else:
    return render_template('new_project.html',project = project,projectcategory=projectcategory)
