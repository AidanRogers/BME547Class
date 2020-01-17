# calculator.py


def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z


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


x = input("Enter a letter: ")
print("You enetered {}".format(x))

if x == "a":
    d = add(50, 50)
    if d > 100:
        print(" your number is too high")

elif x == "s":
    d = subtract(100, 23)
    if d > 100:
        print(" your number is too high")

elif x == "m":
    d = multiply(2, 1)
    if d > 100:
        print(" your number is too high")

elif x == "d":
    d = divide(2, 1)
    if d > 100:
        print(" your number is too high")

else:
    print("The {} command is not recognized.".format(x))

print("Done")
