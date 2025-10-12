num = 123
num2 = num 
S3 = num2 % 10       # S3= 3
S1 = num2 // 100     # S1= 1
Temp = num2 // 10    # Temp= 12
S2 = Temp % 10      # S2= 2 

print(f'Original Sequence : {num}')
print(f'Reverse Sequence : {S3}{S2}{S1}')