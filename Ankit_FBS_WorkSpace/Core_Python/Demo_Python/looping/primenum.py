n = int(input("Enter a num to check whether its prime or not : ")) # n=5
for i in range(2,n): # (2,5) 2,3,4
    if (n % i == 0):
        print(f'{n} is not prime numbers')
        break
else:
    print(f'{n} is prime number ')  


    #here loop break if its not prime and then else part will also not run 
    # because its part of loop and if loop break then else is also break  