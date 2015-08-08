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

projectitem22 = Project(project_url="android_url",
	project_description="This is the sixth project relating to the other category",
	projectname_id="android",
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

comments1 = Comments(content="This first project of FEND is awesome!",author_id=1,project_id=1)
session.add(comments1)
session.commit()

comments2 = Comments(content="This second project of FEND is awesome!",author_id=2,project_id=2)
session.add(comments1)
session.commit()

comments3 = Comments(content="This third project of FEND is awesome!",author_id=3,project_id=3)
session.add(comments3)
session.commit()

comments4 = Comments(content="This fourth project of FEND is awesome!",author_id=4,project_id=4)
session.add(comments4)
session.commit()

comments5 = Comments(content="This fifth project of FEND is awesome!",author_id=5,project_id=5)
session.add(comments5)
session.commit()

comments6 = Comments(content="This sixth project of FEND is awesome!",author_id=5,project_id=6)
session.add(comments6)
session.commit()

comments7 = Comments(content="This first project of FSND is awesome!",author_id=1,project_id=7)
session.add(comments7)
session.commit()

comments8 = Comments(content="This second project of FSND is awesome!",author_id=2,project_id=8)
session.add(comments8)
session.commit()

comments9 = Comments(content="This third project of FSND is awesome!",author_id=3,project_id=9)
session.add(comments9)
session.commit()

comments10 = Comments(content="This fourth project of FSND is awesome!",author_id=4,project_id=10)
session.add(comments10)
session.commit()

comments11 = Comments(content="This fifth project of FSND is awesome!",author_id=5,project_id=11)
session.add(comments11)
session.commit()

comments12 = Comments(content="This first project of iosND is awesome!",author_id=1,project_id=12)
session.add(comments12)
session.commit()

comments13 = Comments(content="This second project of iosND is awesome!",author_id=2,project_id=13)
session.add(comments13)
session.commit()

comments14 = Comments(content="This third project of iosND is awesome!",author_id=3,project_id=14)
session.add(comments14)
session.commit()

comments15 = Comments(content="This fourth project of iosND is awesome!",author_id=4,project_id=15)
session.add(comments15)
session.commit()

comments16 = Comments(content="This fifth project of iosND is awesome!",author_id=5,project_id=16)
session.add(comments16)
session.commit()

comments17 = Comments(content="This first project of androidND is awesome!",author_id=1,project_id=17)
session.add(comments17)
session.commit()

comments18 = Comments(content="This second project of androidND is awesome!",author_id=2,project_id=18)
session.add(comments18)
session.commit()

comments19 = Comments(content="This third project of androidND is awesome!",author_id=3,project_id=19)
session.add(comments19)
session.commit()

comments20 = Comments(content="This fourth project of androidND is awesome!",author_id=4,project_id=20)
session.add(comments20)
session.commit()

comments21 = Comments(content="This fifth project of androidND is awesome!",author_id=5,project_id=21)
session.add(comments21)
session.commit()

comments22 = Comments(content="This sixth project of androidND is awesome!",author_id=1,project_id=22)
session.add(comments22)
session.commit()

comments23 = Comments(content="This first project of Other is awesome!",author_id=2,project_id=23)
session.add(comments23)
session.commit()

comments24 = Comments(content="This second project of Other is awesome!",author_id=3,project_id=24)
session.add(comments24)
session.commit()

comments25 = Comments(content="This third project of Other is awesome!",author_id=4,project_id=25)
session.add(comments25)
session.commit()

comments26 = Comments(content="This fourth project of Other is awesome!",author_id=5,project_id=26)
session.add(comments26)
session.commit()

print "added all items!"