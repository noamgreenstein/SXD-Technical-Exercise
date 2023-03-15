# part 2 programming answer, is also used as part of part 3
def solve_equation(constraints, is_max):
    # solve for x2 first -> no point in seeing which variable is easier to find first
    ratio = constraints[2] / constraints[5]
    x2 = (constraints[4] - (constraints[7] * ratio)) / (
            constraints[3] - (ratio * constraints[6]))
    x1 = (constraints[4] - constraints[3] * x2) / constraints[2]

    # check if constraints are met, if not, raise an exception
    # so the data is not put into table in the database
    if x1 >= 0 and x2 >= 0:
        if is_max:
            # calculate max
            z = max(constraints[0] * x1, constraints[0] * 0) + max(constraints[1] * x2,
                                                                   constraints[1] * 0)
        else:
            # calculate min
            z = min(constraints[0] * x1, constraints[0] * 0) + min(constraints[1] * x2,
                                                                   constraints[1] * 0)
        # for part 2
        print([x1, x2, z])
        return z
    else:
        raise Exception("invalid arguments")


# solve_equation([3, 4, 15, 10, 300, 2.5, 5, 110], True) -> [8.0, 18.0, 96.0] -> this works!
