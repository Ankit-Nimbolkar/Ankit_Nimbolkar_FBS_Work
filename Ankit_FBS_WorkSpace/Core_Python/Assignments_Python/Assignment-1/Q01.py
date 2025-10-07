# Write a program to calculate the percentage of student based on marks of any 5
# subjects.

Eng = int(input("Enter Marks of Eng : "))
Math = int(input("Enter Marks of Math : "))
Geo = int(input("Enter Marks of Geo : "))
Hist = int(input("Enter Marks Of Hist : "))
computer = int(input("Enter Marks of Computer : "))

Total_marks = Eng + Math + Geo + Hist + computer 

percentage = (Total_marks/500)*100

print(type(percentage))
print(f'Percentage of 5 subjects is --> {percentage}')