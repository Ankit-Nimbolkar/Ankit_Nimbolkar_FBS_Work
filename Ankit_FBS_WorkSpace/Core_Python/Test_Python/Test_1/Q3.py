# 3. Write a program to accept distance in km and convert it into meters and
# centimeters both.

Dist = float(input("Enter Distance in KM : "))
Dist_Meter = Dist * 1000   #1km = 1000m   1m = 100cm
Dist_cm = Dist * 100000    #1km = 100000cm

print(f'Distance in KM is {Dist} KM')
print(f'Distance in Meter is {Dist_Meter} M')
print(f'Distance in CM is {Dist_cm} CM')
