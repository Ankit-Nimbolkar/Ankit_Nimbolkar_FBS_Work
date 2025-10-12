# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:) figure is half rectangle and half circle

l=float(input("Enter length in cm :"))
b=float(input("Enter breadth in cm :"))
r=float(input("Enter radius in cm :"))

# figure = half rectangle + semicircle
# Area of figure
# area of rectangle + area of semiciecle
# (length * breadth) + ((1/2)*3.14*r*r)  

#perimeter of figure
#perimeter of rectangle + perimeter of semicircle
# (2*length + breadth)  + 3.14*r

Area = (l*b)+(1/2)*(3.14*r*r)

perimeter = 2*l+ b + 3.14*r

print(f'Area of figure is : {Area} CM')
print(f'Perimeter of figure is : {perimeter} CM')
