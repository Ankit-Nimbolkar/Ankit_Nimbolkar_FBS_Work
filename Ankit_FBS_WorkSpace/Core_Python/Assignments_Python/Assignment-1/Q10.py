# Write a program to calculate area of an equilateral triangle.
import math
Side = int(input("Enter Side of triangle : "))

AreaOfEqiTriangle = (math.sqrt(3)/4)*Side**2

print(f'Area Of Equilateral Triangle is {AreaOfEqiTriangle}')
