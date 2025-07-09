import sqlite3

conn= sqlite3.connect("db1.db") #name kuch bhi de sakte h bas extension .db use karna h

conn.execute('''
Create table users2(usid INTEGER PRIMARY KEY AUTOINCREMENT,
usnm VARCHAR(100),
pass VARCHAR(50),
mobile VARCHAR(15),
email VARCHAR(10)
)
''')
conn.close()

