import math

def aoc(rad):
    return math.pi * rad  ** 2

rad = float(input("Radius: "))
area = aoc(rad)
print("Area of Circle: ", area)
