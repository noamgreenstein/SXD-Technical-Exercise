def solve_equation(constraints, is_max):
    if constraints[2] % constraints[5] == 0:
        ratio = constraints[2] / constraints[5]
        x2 = (constraints[4] - (constraints[7] * ratio)) / (
                constraints[3] - (ratio * constraints[6]))
        x1 = (constraints[4] - constraints[3] * x2) / constraints[2]
    else:
        ratio = constraints[3] / constraints[6]
        x1 = (constraints[4] - (constraints[7] * ratio)) / (
                constraints[2] - (ratio * constraints[5]))
        x2 = (constraints[4] - constraints[2] * x1) / constraints[3]

    if x1 >= 0 and x2 >= 0:
        if is_max:
            z = max(constraints[0] * x1, constraints[0] * 0) + max(constraints[1] * x2,
                                                                   constraints[1] * 0)
        else:
            z = min(constraints[0] * x1, constraints[0] * 0) + min(constraints[1] * x2,
                                                                   constraints[1] * 0)

        print([x1, x2, z])
    else:
        print("no solution")


solve_equation([3, 4, 15, 10, 300, 2.5, 5, 110], True)
