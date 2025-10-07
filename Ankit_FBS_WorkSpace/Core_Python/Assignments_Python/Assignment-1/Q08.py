#Write a program to convert days into years, weeks and days.
total_days = int(input("Enter Total Days : "))

years = total_days//365
Remain_day = total_days%365

weeks = Remain_day//7
days = Remain_day % 7


print(f'{total_days} in years {years} , Weeks {weeks} , days {days}')
