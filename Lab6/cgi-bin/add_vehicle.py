#!/usr/cgi-bin/env python3
import cgi
import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()

form = cgi.FieldStorage()

# Get data from fields
brand = form.getvalue('brand')
model = form.getvalue('model')
year = form.getvalue('year')
price = form.getvalue('price')
owner_id = form.getvalue('owner_id')

c.execute(f"""INSERT INTO vehicles VALUES(
    '{brand}',
    '{model}',
    '{year}',
    '{price}',
    '{owner_id}'
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