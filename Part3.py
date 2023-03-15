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
    min_or_max = input("Min or Max? ")
    while not is_arg(min_or_max.lower()):
        min_or_max = input("Please enter 'Min' or 'Max'? ")

    # make user specify the coefficients for the problem
    # program won't continue if input is invalid
    coeffs = input(f"please enter the two coefficients for the {min_or_max.lower()} statement ")
    coeffs = coeffs.split(" ")
    while len(coeffs) != 2 or not is_number(coeffs[0]) or not is_number(coeffs[1]):
        coeffs = input("invalid arguments please re-enter")
        coeffs = coeffs.split(" ")

    # convert the coefficients into floats
    for i in range(len(coeffs)):
        coeffs[i] = float(coeffs[i])

    # make user specify the coefficients for the first inequality
    eq1 = get_eq("first")

    # make user specify the coefficients for the second inequality
    eq2 = get_eq("second")

    # creating the query to attempt to select the entered values from the table in the database
    select_qry = 'SELECT * FROM SXD WHERE coefficient1 = %s AND coefficient2 = %s ' \
                 'AND eq1_1 = %s AND eq1_2 = %s AND eq1_3 = %s ' \
                 'AND eq2_1 = %s AND eq2_2 = %s AND eq2_3 = %s ' \
                 'AND is_max = %s'

    # attempting to select the entered values from the table in the database
    cursor.execute(select_qry,
                   (coeffs[0], coeffs[1], eq1[0], eq1[1], eq1[2],
                    eq2[0], eq2[1], eq2[2], min_or_max))

    # Check if any rows were returned
    row = cursor.fetchone()
    if row is not None:
        # if it exists let the user know and print the value
        print("already computed")
        print(row[0])
    else:
        # if it does not exist in the database calculate the answer and display it to the user
        is_max = True if min_or_max.lower() == "max" else False
        z = Part2.solve_equation(
            [coeffs[0], coeffs[1], eq1[0], eq1[1], eq1[2], eq2[0], eq2[1], eq2[2]], bool(is_max))
        print(z)

        # define the query to enter the values into the table
        insert_qry = "INSERT INTO SXD (Z, coefficient1, coefficient2, eq1_1, eq1_2, eq1_3, " \
                     "eq2_1, eq2_2, eq2_3, is_max) " \
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # execute the insert query
        cursor.execute(insert_qry, (float(z), coeffs[0], coeffs[1], eq1[0], eq1[1], eq1[2],
                                    eq2[0], eq2[1], eq2[2], min_or_max))

        # commit the changes to the database
        db.commit()


# helper to check if the user entered max or min
def is_arg(arg):
    return arg == "min" or arg == "max"


# helper to check if the user entered a number
def is_number(num):
    num = float(num) if "." in num else int(num)
    return isinstance(num, int) or isinstance(num, float)


# helper to check if the user entered three valid numbers
def is_valid_eq(eq):
    return not (is_number(eq[0]) and is_number(eq[1]) and is_number(eq[2]))


# make user specify the coefficients for a given inequality
# program won't continue if input is invalid
def get_eq(fos):
    eq = input(f"please enter the numbers for the {fos} inequality ")
    eq = eq.split(" ")

    while len(eq) != 3 or is_valid_eq(eq):
        eq = input("invalid arguments please re-enter ")
        eq = eq.split(" ")

    # convert the coefficients into floats
    for j in range(len(eq)):
        eq[j] = float(eq[j])

    return eq


if __name__ == "__main__":
    main()
