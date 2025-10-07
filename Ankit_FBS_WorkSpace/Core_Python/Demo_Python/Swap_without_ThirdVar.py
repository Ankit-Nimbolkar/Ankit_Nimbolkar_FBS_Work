x = int(input("Enter value of x : ")) #10
y = int(input("Enter value of y : ")) #20

print(f'\nValues before swapping are x:{x} and y:{y} \n')

#swapping logic 
x=x+y #10+20=30
y=x-y #30-20 => 10
x=x-y #30-10 => 20

print(f'\nValues After swapping are x:{x} and y:{y} \n')
