import Part2
import mysql.connector


# main method to run the program so user can input their own values
def main():
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

    # make user specify whether they want the min or the max
    # program won't continue if input is invalid
    min_or_max = input("Min or Max?")
    while not is_arg(min_or_max.lower()):
        min_or_max = input(" Please enter 'Min' or 'Max'?")

    # make user specify the coefficients for the problem
    # program won't continue if input is invalid
    coeffs = input(f"please enter the two coefficients for the {min_or_max.lower()} statement")
    coeffs.split(" ")
    while len(coeffs) != 2 or is_number(coeffs[0]) or is_number(coeffs[1]):
        coeffs = input("invalid arguments please re-enter")
        coeffs.split(" ")

    # make user specify the coefficients for the first inequality
    # program won't continue if input is invalid
    eq1 = input("please enter the numbers for the first inequality")
    eq1.split(" ")
    while len(eq1) != 3 or not is_valid_eq(eq1):
        eq1 = input("invalid arguments please re-enter")
        eq1.split(" ")

    # make user specify the coefficients for the second inequality
    # program won't continue if input is invalid
    eq2 = input("please enter the numbers for the second inequality")
    eq2.split(" ")
    while len(eq1) != 3 or not is_valid_eq(eq2):
        eq2 = input("invalid arguments please re-enter")
        eq2.split(" ")

    # creating the query to attempt to select the entered values from the table in the database
    select_qry = 'SELECT * FROM SXD WHERE coefficient1 = coeffs[0] AND coefficient2 = coeffs[1] ' \
                 'AND num1_1 = eq1[0] AND num1_2 = eq1[1] AND num1_3 = eq1[2] ' \
                 'AND num2_1 = eq2[0] AND num2_2 = eq2[1] AND num2_3 = eq2[2] ' \
                 'AND is_max = min_or_max'

    # attempting to select the entered values from the table in the database
    cursor.execute(select_qry)

    # Check if any rows were returned
    row = cursor.fetchone()
    if row is not None:
        # if it exists display the value
        print(row[0])
    else:
        # if it does not exist in the database calculate the answer and display it to the user
        is_max = True if min_or_max.lower() == "max" else False
        z = Part2.solve_equation(
            [float(coeffs[1]), float(coeffs[2]), float(eq1[0]), float(eq1[1]), float(eq1[2]),
             float(eq2[0]), float(eq2[1]), float(eq2[2])],
            bool(is_max))
        print(z)

        # define the query to enter the values into the table
        insert_qry = "INSERT INTO SXD (Z, coefficient1, coefficient2, num1_1, num1_2, num1_3, " \
                     "num2_1, num2_2, num2_3, is_max) " \
                     "VALUES (z, coeffs[1], coeffs[2], eq1[0], eq1[1], eq1[2], " \
                     "eq2[0], eq2[1], eq2[2], min_or_max)"

        # execute the insert query
        cursor.execute(insert_qry)

        # commit the changes to the database
        db.commit()


# helper to check if the user entered max or min
def is_arg(arg):
    return arg == "min" or arg == "max"


# helper to check if the user entered a number
def is_number(num):
    return isinstance(num, int) or isinstance(num, int)


# helper to check if the user entered three valid numbers
def is_valid_eq(eq):
    return is_number(eq[0]) and is_number(eq[1]) and is_number(eq[2])


if __name__ == "__main__":
    main()
