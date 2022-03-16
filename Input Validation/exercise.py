# while True:
# 	print('Enter your age: ')
# 	age = input()
# 	try:
# 		age = int(age)

# 	except:
# 		print('Please use numeric digits.')
# 		continue
# 	if age < 1:
# 		print('Please enter a positive number.')
# 		continue
# 	break

# print(f'Your age is {age}')


##################################################
##################################################
import pyinputplus as pyip

# response = pyip.inputNum('Enter a number: ')
# response = pyip.inputInt(prompt='Enter a number: ')

# response = pyip.inputNum('Enter a number: ', min=4)
# response = pyip.inputNum('Enter a number: ', greaterThan=4)
# response = pyip.inputNum('Enter a number: ', lessThan=6)

##################################################
##################################################
# blank keyword allows for blank inputs

# response = pyip.inputNum('Enter number: ', blank=True)

##################################################
##################################################
# limit, timeout, default

# response = pyip.inputNum('Enter a num: ', limit=2)
# response = pyip.inputNum('Enter a num: ', timeout=2)
# response = pyip.inputNum('Enter a num: ', default='N/A', limit=2)

##################################################
##################################################
# allowregex, blockregex

# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
# 	blockRegexes=[r'cat']
# 	)

##################################################
##################################################
# custom validation function
# def addsUpToTen(numbers):
# 	numbersList = list(numbers)
# 	for i, digit in enumerate(numbersList):
# 		numbersList[i] = int(digit)
# 	if sum(numbersList) != 10:
# 		raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
# 	return int(numbers)

# response = pyip.inputCustom(addsUpToTen)








