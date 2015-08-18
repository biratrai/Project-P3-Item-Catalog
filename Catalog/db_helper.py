# Imports for DB Session
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments

# Connect to the database
engine = create_engine('sqlite:///Catalog/project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def project_list(project,projectcategory):
	"""Get List of Project Names under each Project Category."""
	return session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()

def single_project(project_no):
	"""Get List of Project Names within each Project ID."""
	return session.query(Project).filter_by(project_item_id = project_no).one()

def comments_list(project_no):
	"""Get List of Comments of each Project ID."""
	return session.query(Comments,User).filter(Comments.author_id == User.id).\
    filter(Comments.project_id == project_no).all()

def edit_project(project_no):
	"""Get each Project ID to be edited."""
	return session.query(Project).filter_by(project_item_id = project_no).one()

def delete_project(project_no):
	"""Get each Project ID to be deleted."""
	return session.query(Project).filter_by(project_item_id = project_no).one()

def new_project(url,id,description,project_id,projectcategory,image_url):
	"""Create New Project and return the Project Object."""
	newProject = Project(project_url = url,
		author_id= id,
		project_description= description,
		projectname_id=project_id,
		projectcategory_id=projectcategory,image_url=image_url)
	session.add(newProject)	
	session.commit()
	return newProject

def new_user(user_name,user_email):
	"""Create New User and return the User Object."""
	newUser = User(name=user_name,email=user_email)
	session.add(newUser)	
	session.commit()
	return newUser

def new_comments(comments,id,project_no):
	"""Create New Comments and return the Comments Object."""
	newComment = Comments(content = comments,author_id = id,project_id = project_no)
	session.add(newComment)
	session.commit()
	return newComment

def getUserID(email):
	"""Returns User ID."""
	try:
		user = session.query(User).filter_by(email = email).one()
		return user.id
	except:
		return None

def getUserInfo(user_id):
	"""Returns User ID Object."""
	user = session.query(User).filter_by(id = user_id).one()
	return user

def getUserName(user_id):
	"""Returns User Name Object."""
	user = session.query(User).filter_by(id = user_id).one()
	return user.name  
    
def createUser(login_session):
	"""Create New User and return the User ID Object."""
	newUser = User(name = login_session['username'], email = login_session['email'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email = login_session['email']).one()
	return user.id   

	