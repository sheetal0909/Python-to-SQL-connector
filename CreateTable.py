import mysql.connector

conn = mysql.connector.connect(
host='localhost',
user='root',
password='12345',
database='pythonDB'
)

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE Student (name VARCHAR(50), branch VARCHAR(10), id INT)")

print("Table created successfully")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
