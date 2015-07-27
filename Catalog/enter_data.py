from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Base, User, Project, Comments

# create a session and connect to the DB 
engine = create_engine('sqlite:///project.db')
Base.metadata.reflect(engine)
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

# Fake Data for Users
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

projectitem1 = Project(project_url="frontend_url",
	project_description="This is the first project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem1)
session.commit()	

projectitem2 = Project(project_url="frontend_url",
	project_description="This is the second project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p2",
	author_id=2)
session.add(projectitem2)
session.commit()	

projectitem3 = Project(project_url="frontend_url",
	project_description="This is the third project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p3",
	author_id=3)
session.add(projectitem3)
session.commit()

projectitem4 = Project(project_url="frontend_url",
	project_description="This is the fourth project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p4",
	author_id=4)
session.add(projectitem4)
session.commit()

projectitem5 = Project(project_url="frontend_url",
	project_description="This is the fifth project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p5",
	author_id=5)
session.add(projectitem5)
session.commit()

projectitem6 = Project(project_url="frontend_url",
	project_description="This is the sixth project relating to the FrontEnd Stack",
	projectname_id="frontend",
	projectcategory_id="p6",
	author_id=5)
session.add(projectitem6)
session.commit()

projectitem7 = Project(project_url="frontend_url",
	project_description="This is the first project relating to the Full Stack",
	projectname_id="fullstack",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem7)
session.commit()	

projectitem8 = Project(project_url="frontend_url",
	project_description="This is the second project relating to the Full Stack",
	projectname_id="fullstack",
	projectcategory_id="p2",
	author_id=2)
session.add(projectitem8)
session.commit()	

projectitem9 = Project(project_url="frontend_url",
	project_description="This is the third project relating to the Full Stack",
	projectname_id="fullstack",
	projectcategory_id="p3",
	author_id=3)
session.add(projectitem9)
session.commit()

projectitem10 = Project(project_url="frontend_url",
	project_description="This is the fourth project relating to the Full Stack",
	projectname_id="fullstack",
	projectcategory_id="p4",
	author_id=4)
session.add(projectitem10)
session.commit()

projectitem11 = Project(project_url="frontend_url",
	project_description="This is the fifth project relating to the Full Stack",
	projectname_id="fullstack",
	projectcategory_id="p5",
	author_id=5)
session.add(projectitem11)
session.commit()

projectitem12 = Project(project_url="ios_url",
	project_description="This is the first project relating to the iOS NanoDegree",
	projectname_id="ios",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem12)
session.commit()	

projectitem13 = Project(project_url="ios_url",
	project_description="This is the second project relating to the iOS NanoDegree",
	projectname_id="ios",
	projectcategory_id="p2",
	author_id=2)
session.add(projectitem13)
session.commit()	

projectitem14 = Project(project_url="ios_url",
	project_description="This is the third project relating to the iOS NanoDegree",
	projectname_id="ios",
	projectcategory_id="p3",
	author_id=3)
session.add(projectitem14)
session.commit()

projectitem15 = Project(project_url="ios_url",
	project_description="This is the fourth project relating to the iOS NanoDegree",
	projectname_id="ios",
	projectcategory_id="p4",
	author_id=4)
session.add(projectitem15)
session.commit()

projectitem16 = Project(project_url="ios_url",
	project_description="This is the fifth project relating to the iOS NanoDegree",
	projectname_id="ios",
	projectcategory_id="p5",
	author_id=5)
session.add(projectitem16)
session.commit()

projectitem17 = Project(project_url="android_url",
	project_description="This is the first project relating to the Android Course",
	projectname_id="android",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem17)
session.commit()	

projectitem18 = Project(project_url="android_url",
	project_description="This is the second project relating to the Android Course ",
	projectname_id="android",
	projectcategory_id="p1",
	author_id=2)
session.add(projectitem18)
session.commit()	

projectitem19 = Project(project_url="android_url",
	project_description="This is the third project relating to the Android Course",
	projectname_id="android",
	projectcategory_id="p1",
	author_id=3)
session.add(projectitem19)
session.commit()

projectitem20 = Project(project_url="android_url",
	project_description="This is the fourth project relating to the Android Course",
	projectname_id="android",
	projectcategory_id="p1",
	author_id=4)
session.add(projectitem20)
session.commit()

projectitem21 = Project(project_url="android_url",
	project_description="This is the fifth project relating to the Android Course",
	projectname_id="android",
	projectcategory_id="p1",
	author_id=5)
session.add(projectitem21)
session.commit()

projectitem22 = Project(project_url="other_url",
	project_description="This is the fifth project relating to the other category",
	projectname_id="other",
	projectcategory_id="p1",
	author_id=5)
session.add(projectitem22)
session.commit()

projectitem23 = Project(project_url="other_url",
	project_description="This is the first project relating to the other category",
	projectname_id="other",
	projectcategory_id="p1",
	author_id=1)
session.add(projectitem23)
session.commit()	

projectitem24 = Project(project_url="other_url",
	project_description="This is the second project relating to the other category ",
	projectname_id="other",
	projectcategory_id="p1",
	author_id=2)
session.add(projectitem24)
session.commit()	

projectitem25 = Project(project_url="other_url",
	project_description="This is the third project relating to the other category",
	projectname_id="other",
	projectcategory_id="p1",
	author_id=3)
session.add(projectitem25)
session.commit()

projectitem26 = Project(project_url="other_url",
	project_description="This is the fourth project relating to the other category",
	projectname_id="other",
	projectcategory_id="p1",
	author_id=4)
session.add(projectitem26)
session.commit()





print "added all items!"