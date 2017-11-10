import sqlite3
conn = sqlite3.connect("MyDB.db")
c = conn.cursor()
n = int(input('Enter the number of rows to be inserted: '))
for x in range(n):
    name = input('Enter the name of the student: ')
    grade = float(input('Enter the grade acquired: '))
    c.execute('INSERT INTO stud_grades VALUES(?, ?)',(name, grade))
    conn.commit()

conn.close()
