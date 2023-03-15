import Part2 as p
import mysql.connector


# connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="db.sql"
)