#! python3

import time
import datetime
# print(time.time())

#################################################
# time.time() function

# def calcProd():
# 	# Calculate the product of the first 100,000 numbers
# 	product = 1
# 	for i in range(1, 100000):
# 		product = product * i
# 	return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits longs.' % len(str(prod)))
# print('Took %s seconds to calculate.' % (endTime - startTime))

# Print the time as readable 
# print(time.ctime())
# thisMoment = time.time()
# print(time.ctime(thisMoment))

#################################################
# time.sleep() function

# for i in range(3):
# 	print('Tick')
# 	time.sleep(1)
# 	print('Tock')
# 	time.sleep(1)

#################################################
# Rounding numbers

# now = time.time()
# print(now)
# print(round(now, 2))
# print(round(now, 4))
# print(round(now))

#################################################
# datetime module

# print(datetime.datetime.now())
# dt = datetime.datetime(2019, 10, 21, 16, 29, 0) # first 3 values are year, month, day. Last 3 are hour, minute, second
# print(dt.year, dt.month, dt.day)
# print(dt.hour, dt.minute, dt.second)

# print(datetime.datetime.fromtimestamp(1000000))
# print(datetime.datetime.fromtimestamp(time.time()))

# Comparing dates and times
# halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
# oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
# print(halloween2019 == oct31_2019)
# print(halloween2019 > newyears2020)
# print(newyears2020 > halloween2019)
# print(newyears2020 != oct31_2019)

#################################################
# timedelta Data type

# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))

# Calculate 1000 days from now
# dt = datetime.datetime.now()
# print(dt)
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# print(oct21st)
# print(oct21st - aboutThirtyYears)
# print(oct21st - (2 * aboutThirtyYears))

#################################################
# Pausing until a specific date

# halloween2022 = datetime.datetime(2022, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < halloween2022:
# 	time.sleep(1)

#################################################
# Converting datetime objects into strings

# oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime('%B of %y'))

#################################################
# Converting strings into datetime objects

# print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')) # US string date
# print(datetime.datetime.strptime('21 October, 2019', '%d %B, %Y')) # UK string date
# print(datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '19", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))








