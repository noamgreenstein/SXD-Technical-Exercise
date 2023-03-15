import Part2 as p
import mysql.connector


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

    min_or_max = input("Min or Max?")
    while not is_arg(min_or_max.lower()):
        min_or_max = input(" Please enter 'Min' or 'Max'?")

    coeffs = input(f"please enter the two coefficients for the {min_or_max.lower()} statement")
    coeffs.split(" ")
    while len(coeffs) != 2 or is_number(coeffs[0]) or is_number(coeffs[1]):
        coeffs = input("invalid arguments please re-enter")
        coeffs.split(" ")

    eq1 = input("please enter the numbers for the first inequality")
    eq1.split(" ")
    while len(eq1) != 3 or not is_valid_eq(eq1):
        eq1 = input("invalid arguments please re-enter")
        eq1.split(" ")

    eq2 = input("please enter the numbers for the second inequality")
    eq2.split(" ")
    while len(eq1) != 3 or not is_valid_eq(eq2):
        eq2 = input("invalid arguments please re-enter")
        eq2.split(" ")

    select_qry = 'SELECT * FROM SXD WHERE coefficient1 = coeffs[0] AND coefficient2 = coeffs[1] ' \
           'AND num1_1 = eq1[0] AND num1_2 = eq1[1] AND num1_3 = eq1[2] ' \
           'AND num2_1 = eq2[0] AND num2_2 = eq2[1] AND num2_3 = eq2[2] AND is_max = min_or_max'

    cursor.execute(select_qry)

    row = cursor.fetchone()

    # Check if any rows were returned
    if row is not None:
        print(row[0])
    else:
        is_max = True if min_or_max.lower() == "max" else False
        z = p.solve_equation([coeffs[1], coeffs[2], eq1[0], eq1[1], eq1[2], eq2[0], eq2[1], eq2[2]],
                             is_max)
        print(z)

        # define the SQL statement
        insert_qry = "INSERT INTO SXD (Z, coefficient1, coefficient2, num1_1, num1_2, num1_3, " \
              "num2_1, num2_2, num2_3, is_max) " \
              "VALUES (z, coeffs[1], coeffs[2], eq1[0], eq1[1], eq1[2], eq2[0], eq2[1], eq2[2], " \
              "min_or_max)"

        # execute the SQL statement with the values
        cursor.execute(insert_qry)

        # commit the changes to the database
        db.commit()


def is_arg(arg):
    return arg == "min" or arg == "max"


def is_number(num):
    return isinstance(num, int) or isinstance(num, int)


def is_ineq(ineq):
    return ineq == ">" or ineq == "<" or ineq == "<=" or ineq == ">="


def is_valid_eq(eq):
    return is_number(eq[0]) and is_number(eq[1]) and is_number(eq[2])


if __name__ == "__main__":
    main()
