# Write a Program to input two angles from user and find third angle of the
# triangle.

Ang1 = int(input("Enter Angle_1 : "))
Ang2 = int(input("Enter Angle_2 : "))

Sum = Ang1 + Ang2
Third_Angle = 180 - Sum

print(f'Angle_1 is {Ang1} \n Angle_2 is {Ang2} \n Angle_3 is {Third_Angle}')