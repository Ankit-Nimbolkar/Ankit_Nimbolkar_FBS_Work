# Write a program to enter P, T, R and calculate simple Interest.
P = int(input("Enter the Principle Amount : "))
R = float(input("Enter The Annual Interest Rate :"))
T = int(input("Enter Time Period : "))

simple_interest = (P*R*T)/100

print(int(simple_interest))