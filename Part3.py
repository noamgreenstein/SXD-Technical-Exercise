# import Part2 as p
import mysql.connector


def main():
    min_or_max = input("Min or Max?")
    while not is_arg(min_or_max.lower()):
        min_or_max = input(" Please enter 'Min' or 'Max'?")

    coeffs = input(f"please enter the two coefficients for the {min_or_max.lower()} statement")
    coeffs.split(" ")
    while len(coeffs) != 2 or is_number(coeffs[0]) or is_number(coeffs[1]):
        coeffs = input("invalid arguments please re-enter")
        coeffs.split(" ")

    eq1 = input("please enter the first inequality without the variables")
    eq1.split(" ")
    while len(eq1) != 4 or not is_valid_eq(eq1):
        eq1 = input("invalid arguments please re-enter")
        eq1.split(" ")

    eq2 = input("please enter the second inequality without the variables")
    eq2.split(" ")
    while len(eq1) != 4 or not is_valid_eq(eq2):
        eq2 = input("invalid arguments please re-enter")
        eq2.split(" ")

    # check if database entry exists - return Z
    # if not - calculate Z and add it to the database

def is_arg(arg):
    return arg == "min" or arg == "max"


def is_number(num):
    return isinstance(num, int) or isinstance(num, int)


def is_ineq(ineq):
    return ineq == ">" or ineq == "<" or ineq == "<=" or ineq == ">="


def is_valid_eq(eq):
    return is_number(eq[0]) and is_number(eq[1]) and is_ineq(eq[2]) and is_number(eq[3])


if __name__ == "__main__":
    main()

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

# execute the SQL statement with the values
cursor.execute(sql)

# commit the changes to the database
db.commit()

# print the number of rows affected
print(cursor.rowcount, "record inserted.")
