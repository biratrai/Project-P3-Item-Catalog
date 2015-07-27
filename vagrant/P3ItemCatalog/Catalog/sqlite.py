import sqlite3, os 
from flask import g, Flask , current_app, request, session, _app_ctx_stack
#from Catalog import app

app = Flask(__name__)

#DATABASE = 'os.path.join(app.root_path, 'project.db')'
DATABASE = '/vagrant/P3ItemCatalog/Catalog/project.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

for user in query_db('select * from users'):
    print user['name'], 'has the id', user['id']            

