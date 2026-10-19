import mysql.connector

conn = mysql.connector.connect(
host='localhost',
user='root',
password='12345'
)

mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS pythonDB")

print("Database pythonDB created successfully")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

