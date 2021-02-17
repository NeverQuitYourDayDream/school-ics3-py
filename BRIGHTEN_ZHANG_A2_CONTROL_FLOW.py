# Quadratic Equation Solver
# QES finds the real roots of quadratic equations
# of the form ax^2 + bx + c = 0,
# with a being a non-zero integer
# Created on 2/17/2021 by Brighten Zhang

import math
from math import sqrt

print("-------------------------------------------------------")
print("============== Quadratic Equation Solver ==============")
print("-------------------------------------------------------")
print("QES finds the real roots of Quadratic equations of the \nform ax^2 + bx + c = 0")

another = 'y'
while another == 'y':

    # get values of a, b, c from user input
    a, b, c = map(
        float,
        input("\nEnter space-seperated values for a, b, c: ").split())

    # print the equation so that users can see
    # what equation we're dealing with

    # turn any floats into int if possible
    if int(a) == a:
        a = int(a)
    if int(b) == b:
        b = int(b)
    if int(c) == c:
        c = int(c)

    constants = [a, b, c]
    result = [str(a)]
    for i in constants[1:]:
        if i > 0:
            result.append('+ ' + str(i))

            # don't worry about i == 0
            # that will not be written in
            # the equation
        elif i < 0:
            result.append('- ' + str(abs(i)))
        else:
            result.append('')

	# print the equation
    if b != 0:
        print("\nThe equation is {0}x^2 {1}x {2} = 0\n".format(
            result[0], result[1], result[2]))
    else:
        print("\nThe equation is {0}x^2 {1} = 0\n".format(
            result[0], result[2]))

    # discriminant D = b^2 - 4ac
    # if D > 0 then there are 2 real solutions
    # elif D == 0 then there is only 1 real solution
    # else no solutions
    # a != 0 so ZeroDivisionError is not a problem

    D = b * b - 4 * a * c
    real_roots = 0
    if D > 0:
        real_roots = 2
        print("There are 2 solutions.")
    elif D == 0:
        real_roots = 1
        print("There is 1 solution.")
    else:
        real_roots = 0
        print("There are no solutions.")

    # real roots are found using the quadratic equation

    # if there's 2 real roots
    # let x1 be first soltion taking +
    # let x2 be second solution taking -
    if real_roots == 2:
        x1 = round((-b + sqrt(b * b - 4 * a * c)) / (2 * a), 3)
        x2 = round((-b - sqrt(b * b - 4 * a * c)) / (2 * a), 3)
        if int(x1) == x1:
            x1 = int(x1)
        if int(x2) == x2:
            x2 = int(x2)
        print("The two solutions are\nx = {0} and \nx = {1}".format(x1, x2))
    elif real_roots == 1:
        # D = 0
        x = round((-b) / (2 * a), 3)
        if int(x) == x:
            x = int(x)
        print("The solution is x = {}".format(x))
    else:
        # there are no solutions so we're done
        pass

    another = input("\nEnter another equation? y/n: ")
    if another == 'n':
        print("\nThank you for using this calculator, have a nice day.")
