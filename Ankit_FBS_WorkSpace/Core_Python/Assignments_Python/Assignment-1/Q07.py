# Program to Find the Roots of a Quadratic Equation
import math 
a = int(input("Enter Coefficient a : "))
b = int(input("Enter Coefficient b : "))
c = int(input("Enter Coefficient c : "))

D =  ((b**2) - (4*a*c))
print(D)

if D>0:
    root1 = (-b + math.sqrt(D))/(2*a)
    root2 = (-b - math.sqrt(D))/(2*a)
    print(f'Root 1 is {root1}')
    print(f'Root 2 is {root2}')

elif D==0:
    root = -b / (2*a)
    print(f'Roots are same {root}')

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-D) / (2*a)
    print("Roots are complex")
    print(f'Root1 is {real}+{imaginary}i')
    print(f'Root1 is {real}-{imaginary}i')



          


