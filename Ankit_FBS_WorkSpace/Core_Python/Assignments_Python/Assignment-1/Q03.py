#  Program to find quotient and remainder of two numbers.
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

#Quotient
Quotient = num1//num2 

#Remainder
Remainder = num1%num2

print(f'Quotient of {num1} and {num2} is {Quotient}')
print(f'Remainder of {num1} and {num2} is {Remainder}')