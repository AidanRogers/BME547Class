# calculator.py

import math

def add(x, y):
    z = x + y
    symbol = "+"
    #print("{} + {} = {}".format(x, y, z))
    return z, symbol


def subtract(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z


def multiply(x, y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))
    return z


def divide(x, y):
    z = x / y
    print("{} / {} = {}".format(x, y, z))
    return z

def square_root(x):
    import math
    z = math.sqrt(x)
    print("squareroot {} = {}".format(x, z))
    return z

print("you're going to input a letter for a calculator function --> a - Add, s - Subtract, m - Multiply, d - Divide, r - Square Root")
x = input("Enter a letter: ")
num1 = input("Enter the first number you want to manipulate: ")
num2 = input("Enter the first number you want to manipulate: ")
num1 = int(num1)
num2 = int(num2)
print("You entered {}".format(x, num1, num2))

if x == "a":
    d, f = add(num1, num2)
    print("{} {} {} = {}".format(num1, f, num2, d))
    if d == None:
            print("I forgot a variable in add()")

elif x == "s":
    d = subtract(num1, num2)
    print(d)
    if d == None:
        print("I forgot a variable in add()")

elif x == "m":
    d = multiply(num1, num2)
    print(d)
    if d == None:
        print("I forgot a variable in add()")

elif x == "d":
    d = divide(num1, num2)
    print(d)
    if d == None:
        print("I forgot a variable in add()")

elif x == "r":
    d = square_root(num1)
    print(d)
    if d == None:
        print("I forgot a variable in add()")

else:
    print("The {} command is not recognized.".format(x))

print("Done")
