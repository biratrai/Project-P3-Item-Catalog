for instance in session.query(projectnames).order_by(projectnames.id): 
	print instance.name, instance.description, instance.id

for table in Base.metadata.tables.values():
	print type(table)
	rows = session.query(table).all()	
	print rows



for project in project('select * from projectnames'):
    print project['name'], 'has the id', project['id'], 'description ',project['description']	




import sqlite3
conn = sqlite3.connect('project.db')
c = conn.cursor()

print c.execute("SELECT * FROM projectnames")
print c.fetchall()

c.execute("SELECT * FROM user")
print c.fetchall()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())


3
4
# Get a cursor object
cursor.execute('''DROP TABLE users''')
db.commit()

c.execute("SELECT * FROM projectitems")
for i in c.fetchall():
	print i
    
c = session.query(Project).filter_by(projectname_id = "fend")
for i in c:
	print "project item id: "i.project_item_id
	print "project url: "i.project_url
	print "project category id: "i.projectcategory_id
	print "author id: "i.author_id
	print "project name id: "i.projectname_id
	print "\n"