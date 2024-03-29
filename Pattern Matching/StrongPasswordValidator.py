import re

def strongPassword(password):
	password_number = re.compile(r'[0-9]+')
	pw_number = password_number.search(password)

	password_capital = re.compile(r'[A-Z]+')
	pw_capital = password_capital.search(password)

	password_letter = re.compile(r'[a-z]+')
	pw_letter = password_letter.search(password)

	print(password_number.search(password) != None)
	print(password_capital.search(password) != None)
	print(password_letter.search(password) != None)

	if ((password_number.search(password) != None) and (password_capital.search(password) != None) and 
		(password_letter.search(password) != None) == True):
		print('Valid')
	else:
		print('This password is too weak. ')
		return False

	# at least 8 chars long
	if len(password) < 8:
		print(f'{password}: length too short')
		return False

pword = input('Enter your password: ')
strongPassword(pword)