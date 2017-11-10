import sqlite3
conn = sqlite3.connect("MyDB.db")
c = conn.cursor()
c.execute('CREATE TABLE stud_grades(stud_name VARCHAR, grade NUMBER)')
c.close()
