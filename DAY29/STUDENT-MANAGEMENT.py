import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
               roll INTEGER PRIMARY KEY,
               name TEXT,
               marks INTEGER
               )""")

def add_student(roll,name,marks):
    cursor.execute("INSERT INTO student VALUES (?,?,?)",(roll,name,marks))
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()
    for row in records:
        print(row)

add_student(1,"Anuj",75)
view_students()

conn.close()