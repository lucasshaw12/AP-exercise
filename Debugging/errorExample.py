#! python3

# An example of how call stack display error messages (i.e tracebacks)
# def spam():
# 	bacon()

# def bacon():
# 	raise Exception('This is the error message')

# spam()


# Writing a traceback error to a .txt file
# import traceback
# try:
# 	raise Exception('This is the error message')
# except:
# 	errorFile = open('errorInfo.txt', 'w')
# 	errorFile.write(traceback.format_exc())
# 	errorFile.close()
# 	print('The traceback info was written to errorInfo.txt')

# Assertions
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.sort()
# print(ages)
# assert ages[0] <= ages[-1] # confirms the the first number <= the last number after sorting

# # Assertions
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# print(ages)
# assert ages[0] <= ages[-1] # confirms the the first number <= the last number after sorting, this should error as the order was reversed

# Assertions within a function
# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}

# def switchLights(stoplight):
# 	for key in stoplight.keys():
# 		if stoplight[key] == 'green':
# 			stoplight[key] = 'yellow'
# 		if stoplight[key] == 'yellow':
# 			stoplight[key] = 'red'
# 		if stoplight[key] == 'red':
# 			stoplight[key] = 'green'

# 	assert 'red' in stoplight.values(), 'Neither light is red ' + str(stoplight)

# switchLights(market_2nd)