import math

x = int(input("Introduceti nr: "))


def fOne(x):
    return abs(x) * (x ** 3)

def fTwo(x):
    return math.log10(x) + math.log(x)

def fThree(x):
    return math.sin(x) + (math.sin(x) * math.cos(x))

def fFour(x):
    return math.exp(x) + 2 * math.atan(x) - x


print("Functia 1 = {}, \n"
      "Functia 2 = {}, \n"
      "Functia 3 = {}, \n"
      "Functia 4 = {}".format(fOne(x), fTwo(x), fThree(x), fFour(x)))
