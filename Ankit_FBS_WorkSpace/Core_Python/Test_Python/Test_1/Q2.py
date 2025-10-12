# Q2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)

Principal = int(input("Enter Principal Amount : "))
Rate = float(input("Enter Rate of interest : "))
Time = int(input("Enter Time Period : "))

Simple_Interest = Principal * Rate * Time / 100

print(f'Simple Interest For {Time} years  on {Rate} %  Rate is {Simple_Interest}')

