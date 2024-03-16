# import sqlite3
#
# db = sqlite3.connect('database.db')
# c = db.cursor()
# #
# c.execute("""CREATE TABLE vehicles(
#     brand VARCHAR(50) NOT NULL,
#     model VARCHAR(120) NOT NULL,
#     year YEAR NOT NULL,
#     price INT NOT NULL,
#     owner_id INT NOT NULL,
#     FOREIGN KEY (owner_id) REFERENCES users(rowid)
# )""")
#
# c.execute("""CREATE TABLE auto_parts(
#     manufacturer VARCHAR(50) NOT NULL,
#     name VARCHAR(120) NOT NULL,
#     price INT NOT NULL,
#     seller_id INT NOT NULL,
#     FOREIGN KEY (seller_id) REFERENCES users(rowid)
# )""")
#
# c.execute("""CREATE TABLE users(
#     first_name VARCHAR(50) NOT NULL,
#     last_name VARCHAR(120) NOT NULL,
#     login VARCHAR(50) NOT NULL,
#     pass_hash VARCHAR(50) NOT NULL
# )""")
#
# # add users
# c.execute("""INSERT INTO users VALUES(
#     'Robert',
#     'Smith',
#     'robsm',
#     '2er552'
# )""")
# c.execute("""INSERT INTO users VALUES(
#     'John',
#     'No',
#     'jonno',
#     'g32kfmr4'
# )""")
#
# # add vehicles
# c.execute("""INSERT INTO vehicles VALUES(
#     'Lola',
#     'Penske Sunoco T70 MKIIIB',
#     '1969',
#     '325805',
#     '1'
# )""")
# c.execute("""INSERT INTO vehicles VALUES(
#     'Nissan',
#     'Versa',
#     '2024',
#     '16390',
#     '1'
# )""")
# c.execute("""INSERT INTO vehicles VALUES(
#     'Kia',
#     'Telluride',
#     '2024',
#     '36190',
#     '2'
# )""")
#
# # add auto_parts
# c.execute("""INSERT INTO auto_parts VALUES(
#     'Toyo Tiers',
#     'Tiers',
#     '575',
#     '1'
# )""")
# c.execute("""INSERT INTO auto_parts VALUES(
#     'Bride',
#     'Steering Wheel',
#     '305',
#     '2'
# )""")
# c.execute("""INSERT INTO auto_parts VALUES(
#     'Bride',
#     'Seat',
#     '430',
#     '2'
# )""")
#
# # c.execute("DELETE FROM cars WHERE rowid > 3")
# c.execute("SELECT rowid, * FROM vehicles")
# vehicles = c.fetchall()
# for v in vehicles:
#     print(f"\n{v[0]}\n{v[1]}\n{v[2]}\n{v[3]}\n{v[4]}\n{v[5]}")
#
# c.execute("SELECT rowid, * FROM auto_parts")
# auto_parts = c.fetchall()
# for ap in auto_parts:
#     print(f"\n{ap[0]}\n{ap[1]}\n{ap[2]}\n{ap[3]}\n{ap[4]}")
#
# c.execute("SELECT rowid, * FROM users")
# users = c.fetchall()
# for user in users:
#     print(f"\n{user[0]}\n{user[1]}\n{user[2]}\n{user[3]}\n{user[4]}")
#
# c.execute("UPDATE users SET last_name = 'Navarro' WHERE rowid = 2")
#
# c.execute("""INSERT INTO users VALUES(
#     'Tim',
#     'Wald',
#     'twkd',
#     '243k21'
# )""")
# c.execute("""INSERT INTO users VALUES(
#     'Paul',
#     'Kasd',
#     'dkkes',
#     '32k60s'
# )""")
# c.execute("""INSERT INTO vehicles VALUES(
#     'BM',
#     'Trsafl',
#     '2024',
#     '33211',
#     '3'
# )""")
# c.execute("""INSERT INTO vehicles VALUES(
#     'Rasdf',
#     'Hosfk',
#     '2020',
#     '29492',
#     '2'
# )""")
# c.execute("""INSERT INTO auto_parts VALUES(
#     'Tiqqds',
#     'Tiers',
#     '235',
#     '4'
# )""")
# c.execute("""INSERT INTO auto_parts VALUES(
#     'Loddoa',
#     'Seat',
#     '789',
#     '1'
# )""")
# db.commit()
# db.close()