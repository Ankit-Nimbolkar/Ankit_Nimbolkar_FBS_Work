#numbers from 1-10
# for i in range(1,11):
#     print(i)

#Numbers from 1-10 by step of 2
# for i in range(1,11,2):
#     print(i)

#multiplication table
# n = int(input("Enter numbers whose table to print : "))
# for i in range(n,n*10+1,n):
#     print(i)

#Reverse numbers from 10-1
# for i in range(10,0,-1):
#     print(i)

#Reverse numbers from 45-37
# for i in range(45,36,-1):
#     print(i)

#Reverse Multiplication table
# n = int(input("Enter number whose table you want to print in reverse : "))

#1st method
# for i in range(n*10,0,-n):
#     print(i)

#2nd method
# for i in range(1,11):
#     print(i*n)

#3rd method
# for i in range(10,0,-1):
#     print(i*n)


# for i in range(5):
#     print(i)


#sum of first n natural numbers
# n = int(input("Enter number : "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)    
 

#factorial 
n = int(input("Enter number : "))
temp=1
for i in range(n,0,-1):
    temp=temp*i
print(f'Factorial of {n} is {temp}')

