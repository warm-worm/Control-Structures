###
# Checks if the given day number of the month is correct
#
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
year = int(input('Enter the year: '))
day_ok = False

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if day >=1 and day <= 31:
        day_ok = True
elif month==4 or month==6 or month==9 or month==11:
    if day >=1 and day <= 30:
        day_ok = True
elif month==2:
     leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
     if leap_year and day==29:
        day_ok = True
     elif day >=1 and day <=28:
         day_ok = True
        

message = f'Day {day} for the month {month} and year {year}'
if day_ok:
    print(f'{message} is correct.')
else:
    print(f'{message} is incorrect.')
