import mysql.connector

conn = mysql.connector.connect(
host='localhost',
user='root',
password='12345',
database='pythonDB'
)

mycursor = conn.cursor()

sql = 'INSERT INTO Student (name, branch, id) VALUES (%s, %s, %s)'

val = [
('Rohit', 'CSE', 75),
('Viral', 'IT', 83),
('Sachin', 'ELE', 77)
]

mycursor.executemany(sql, val)

conn.commit()

print(mycursor.rowcount, 'Records Inserted')

#mycursor.close()
#conn.close()
