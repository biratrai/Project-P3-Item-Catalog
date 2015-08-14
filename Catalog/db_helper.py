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
	return session.query(Project).filter_by(projectname_id = project,projectcategory_id=projectcategory).all()

def single_project(project_no):
	return session.query(Project).filter_by(project_item_id = project_no).one()

def comments_list(project_no):
	return session.query(Comments,User).filter(Comments.author_id == User.id).\
    filter(Comments.project_id == project_no).all()

def edit_project(project_no):
	return session.query(Project).filter_by(project_item_id = project_no).one()

def delete_project(project_no):
	return session.query(Project).filter_by(project_item_id = project_no).one()

def new_project(url,id,description,project_id,projectcategory):
	newProject = Project(project_url = url,
		author_id= id,
		project_description= description,
		projectname_id=project_id,
		projectcategory_id=projectcategory)
	session.add(newProject)	
	session.commit()
	return newProject

def new_comments(comments,id,project_no):
	newComment = Comments(content = comments,author_id = id,project_id = project_no)
	session.add(newComment)
	session.commit()
	return newComment

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

	