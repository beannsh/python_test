import maths

x = [2, 4, 6]

print (x)


def prumer(x):
    total = 0
    number_of_integers = 0
    for item in x:
        total = total + item
        number_of_integers = number_of_integers + 1
    prumer = total / number_of_integers
    return round(prumer, 2)

print (prumer)

