x = int(input("Enter value of x : ")) #10
y = int(input("Enter value of y : ")) #20

print(f'\nValues before swapping are x:{x} and y:{y} \n')

x,y=y,x
print(f'\nValues After swapping are x:{x} and y:{y} \n')


#-----How Logic Work-------
# What actually happens:
# x, y = y, x works in two phases:
# Right-hand side is evaluated first
# y, x becomes (20, 10)
# Python creates a tuple (20, 10) and stores it temporarily.
# Left-hand side unpacking
# x, y = (20, 10)
# So x = 20 and y = 10.