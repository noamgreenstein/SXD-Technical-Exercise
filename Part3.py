# import Part2 as p
import mysql.connector


# connect to the database
db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="eBs+PKy8c6Rl7971lvcAXktDIEy2ZbbA",
    database="exercise"
)

# create a cursor object
cursor = db.cursor()

# define the SQL statement
sql = "INSERT INTO SXD (Z, equation, max) VALUES (10, 'hello brother', 'TRUE')"

# define the values to insert
# values = (10, "hello brother", "TRUE")

# execute the SQL statement with the values
cursor.execute(sql)

# commit the changes to the database
db.commit()

# print the number of rows affected
print(cursor.rowcount, "record inserted.")