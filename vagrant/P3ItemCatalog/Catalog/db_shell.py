from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Project, Comments


engine = create_engine('sqlite:///project.db')
Base.metadata.reflect(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

print('Your SQLAlchemy session is ready to go! Access it with `session`')
print Base.metadata.tables.keys()

# print Base.metadata.tables['projectitems']
# print Base.metadata.tables['users']
# print Base.metadata.tables['comments']

# for table in Base.metadata.tables.values():
# 	print type(table)
# 	# rows = session.query(table).all()	
# 	# print rows
# 	print table

# for t in Base.metadata.sorted_tables:
# 	print t.name

#print User.query.all()	
project_list = session.query(Project).filter_by(project_item_id = "fend",projectcategory_id="p1").all()
print project_list
# print type(project_list),"project list: ", project_list, "\n"
for i in project_list:
	#print i
	print "project item id: ", i.project_item_id
	print "project url: ", i.project_url
	print "project category id: ", i.projectcategory_id
	print "author id: ", i.author_id
	print "project name id: ", i.projectname_id
	print "\n"

# user1 = session.query(User).order_by(asc(User.name)).all()
# print user1	

# user1 = session.query(User).order_by(asc(User.name))
# print type(user1),user1

#print users.columns.id	
