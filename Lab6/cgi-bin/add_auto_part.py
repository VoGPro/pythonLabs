#!/usr/cgi-bin/env python3
import cgi
import sqlite3

db = sqlite3.connect('database.db')
c = db.cursor()

form = cgi.FieldStorage()

# Get data from fields
manufacturer = form.getvalue('manufacturer')
name = form.getvalue('name')
price = form.getvalue('price')
seller_id = form.getvalue('seller_id')

c.execute(f"""INSERT INTO auto_parts VALUES(
    '{manufacturer}',
    '{name}',
    '{price}',
    '{seller_id}'
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