# Date validity checker

import re

# Set the expression for the var date
date = input('Please enter a date in the following format DD-MM-YYYY')

# Groups the expression into day, month, year
date_detect_regex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
dt = date_detect_regex.search(date)

day, month, year = dt.groups()
print('Chosen date: ' + str(dt.group()) + '\n')

# Detect whether 'day', 'month' and 'year' are valid dated
if day > str(31):
	print('This day is not valid: ', day)

else:
	print('This day is valid: ', day)

if month > str(12):
	print('This month is not valid: ', month)

else:
	print('This month is valid: ', month)

if year > str(2999) or year < str(1000):
	print('This year is not valid: ', year)

else:
	print('This year is valid: ', year)

# Set valid dates for each specific monmths
if month == '04' or month == '06' or month == '09' or month == '11':
	if day > str(30):
		print('This month only has 30 days, this day is invalid')

if month == '02':
	if day > '28':
		print('February only has 28 days, this day is invalid')

if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
	if day > '31':
		print('This month only has 31 days, this day is invalid')

# Check whether that year is a leap year
if int(year) % 4 == 0 or int(year) % 100 == 0 or int(year) % 400 == 0:
	print(f'{year} is a leap year')
else:
	print(f'{year} is not a leap year')

