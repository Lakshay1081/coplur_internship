import  sqlite3

conn=sqlite3.connect("db1.db")

execute("UPDATE users set usnm 'XYZ' where usid=1 ")