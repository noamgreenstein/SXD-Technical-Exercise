# import Part2 as p
import mysql.connector


# connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="db.sql"
)

# create a cursor object
cursor = db.cursor()

# define the SQL statement
sql = "INSERT INTO SXD (Z, equation, max) VALUES (%f, %s, %s)"

# define the values to insert
values = (10, "hello brother", "TRUE")

# execute the SQL statement with the values
cursor.execute(sql, values)

# commit the changes to the database
db.commit()

# print the number of rows affected
print(cursor.rowcount, "record inserted.")