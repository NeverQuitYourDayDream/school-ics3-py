# Multiplication Table
# Asks user for the number of rows and columns and
# Prints out a multiplication table of that size
# Created on 2/18/2021 by Brighten Zhang

print("----------------------------------")
print("=====| Multiplication Table |=====")
print("----------------------------------")

another = 'y'
while another == 'y':

    while True:
        try:
            rows = int(input("\nEnter the number of rows: "))
            if rows > 20 or rows < 1:
                print(
                    "The number of rows must be a\npositive integer not greater than 20."
                )
                raise ValueError
            break
        except ValueError:
            print("Invalid input, try again.")

    while True:
        try:
            columns = int(input("Enter the number of columns: "))
            if columns > 20 or columns < 1:
                print(
                    "The number of columns must be a\npositive integer not greater than 20."
                )
                raise ValueError
            break
        except ValueError:
            print("Invalid input, try again.")

    print("\nMultiplication Table with {0} rows and {1} columns: ".format(
        rows, columns))
    print("\n")
    print("    ", end='')
    for i in range(1, columns + 1):
        print("{:>{w}}".format(i, w=5), end='')
    print("")
    print('   -' + '-----' * (columns))

    for i in range(1, rows + 1):
        print("{:>2}| ".format(str(i)), end='')

        for j in range(1, columns + 1):
            print("{:>{w}}".format(str(i * j), w=5), end='')
        print("\n")

    while True:
        try:
            another = input("Try another table? y/n: ")
            if another == 'y':
                break
            elif another == 'n':
                print("\nThank you for using this multiplication table.")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, try again.")
