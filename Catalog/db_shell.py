from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments


engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

print('Your SQLAlchemy session is ready to go! Access it with `session`')
#print Base.metadata.tables.keys()
#print Base.metadata.tables['projectnames']

for t in Base.metadata.sorted_tables:
	print t.name

#print User.query.all()	
project_list = session.query(Project).filter_by(projectname_id = "fend",projectcategory_id="p1")
for i in project_list:
	print i
	print "project item id: ", i.project_item_id
	print "project url: ", i.project_url
	print "project category id: ", i.projectcategory_id
	print "author id: ", i.author_id
	print "project name id: ", i.projectname_id
	print "\n"

#print users.columns.id	
