num1 = int(input("Enter Num1 : ")) #10
num2 = int(input("Enter Num2 : ")) #20
Place_holder = None 

print(f'Value Before Swapping num1 = {num1}  and num2 = {num2}')

#Swapping
Place_holder = num1 # store 10 in Placeholder
num1 = num2  # store 20 in num1
num2 = Place_holder  #store 10 in num2

print(f'\n Values after Swapping \n')
print(f'value of num1 = {num1}')
print(f'value of num2 = {num2}')