from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, User, Project, Comments

# create a session and connect to the DB 
engine = create_engine('sqlite:///project.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Menu for FSND
user1 = User(name="Santi",email="santi@gmail.com")
session.add(user1)
session.commit()

user2 = User(name="Robert",email="robert@gmail.com")
session.add(user2)
session.commit()

user3 = User(name="Dennis",email="dennis@gmail.com")
session.add(user3)
session.commit()

user4 = User(name="Arsene",email="arsene@gmail.com")
session.add(user4)
session.commit()

user5 = User(name="Jack",email="jack@gmail.com")
session.add(user5)
session.commit()

# project1 = ProjectName(name = "frontend",description="frontend project")
# session.add(project1)
# session.commit()

# project2 = ProjectName(name = "frontend",description="frontend project")
# session.add(project2)
# session.commit()

# project3 = ProjectName(name = "ios",description="ios project")
# session.add(project3)
# session.commit()

# project4 = ProjectName(name = "android",description="android project")
# session.add(project4)
# session.commit()

# project5 = ProjectName(name = "others",description="Others project")
# session.add(project5)
# session.commit()

projectitem1 = Project(project_url="frontend_url",
	project_description="This is the first project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem1)
session.commit()	

projectitem2 = Project(project_url="frontend_url",
	project_description="This is the second project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p2",
	author_id=2)
session.add(projectitem2)
session.commit()	

projectitem3 = Project(project_url="frontend_url",
	project_description="This is the third project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p3",
	author_id=3)
session.add(projectitem3)
session.commit()

projectitem4 = Project(project_url="frontend_url",
	project_description="This is the fourth project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p3",
	author_id=4)
session.add(projectitem4)
session.commit()

projectitem5 = Project(project_url="frontend_url",
	project_description="This is the fifth project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p5",
	author_id=5)
session.add(projectitem5)
session.commit()

projectitem6 = Project(project_url="frontend_url",
	project_description="This is the sixth project relating to the FrontEnd Stack",
	projectname_id="fend",
	projectcategory_id="p6",
	author_id=5)
session.add(projectitem6)
session.commit()

projectitem7 = Project(project_url="frontend_url",
	project_description="This is the first project relating to the Full Stack",
	projectname_id="fsnd",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem7)
session.commit()	

projectitem8 = Project(project_url="frontend_url",
	project_description="This is the second project relating to the Full Stack",
	projectname_id="fsnd",
	projectcategory_id="p2",
	author_id=2)
session.add(projectitem8)
session.commit()	

projectitem9 = Project(project_url="frontend_url",
	project_description="This is the third project relating to the Full Stack",
	projectname_id="fsnd",
	projectcategory_id="p3",
	author_id=3)
session.add(projectitem9)
session.commit()

projectitem10 = Project(project_url="frontend_url",
	project_description="This is the fourth project relating to the Full Stack",
	projectname_id="fsnd",
	projectcategory_id="p3",
	author_id=4)
session.add(projectitem10)
session.commit()

projectitem11 = Project(project_url="frontend_url",
	project_description="This is the fifth project relating to the Full Stack",
	projectname_id="fsnd",
	projectcategory_id="p5",
	author_id=5)
session.add(projectitem11)
session.commit()


# projectitem3 = Project(project_url="frontend_url",project_description="This is the third project relating to the FrontEnd Stack",
# 	projectname_id="fend",
# 	projectcategory_id="p3",
# 	author_id=1)
# session.add(projectitem3)
# session.commit()

# projectitem2 = ProjectItem(project_url="fullstack_url",project_description="This is the project relating to the Fullstack",
# 	author=2)
# session.add(projectitem2)
# session.commit()	

# projectitem3 = ProjectItem(project_url="ios_url",project_description="This is the project relating to the ios",
# 	author=3)
# session.add(projectitem3)
# session.commit()	

# projectitem4 = ProjectItem(project_url="android_url",project_description="This is the project relating to the Android",
# 	author=4)
# session.add(projectitem4)
# session.commit()	

# projectitem5 = ProjectItem(project_url="other_url",project_description="This is the project relating to the other project",
# 	author=5)
# session.add(projectitem5)
# session.commit()	

# comments1 = Comments(content="This is a awesome project",author=1,project=1)
# session.add(comments1)
# session.commit()

# comments2 = Comments(content="This is a awesome project",author=2,project=2)
# session.add(comments2)
# session.commit()

# comments3 = Comments(content="This is a awesome project",author=3,project=3)
# session.add(comments3)
# session.commit()

# comments4 = Comments(content="This is a awesome project",author=4,project=4)
# session.add(comments4)
# session.commit()

# comments5 = Comments(content="This is a awesome project",author=5,project=5)
# session.add(comments5)
# session.commit()

print "added all items!"