#!/usr/cgi-bin/env python3
import cgi
import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()

form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
login = form.getvalue('login')
pass_hash = form.getvalue('pass_hash')

c.execute(f"""INSERT INTO users VALUES(
    '{first_name}',
    '{last_name}',
    '{login}',
    '{pass_hash}'
)""")

db.commit()
db.close()

print('Content-type:text/html\n\n')
redirectURL = "http://localhost:8000/cgi-bin/site.py"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
print('  </head>')
print('</html>')