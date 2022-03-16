myCat = {'size': 'fat', 'colour': 'grey', 'disposition': 'loud' }

print(myCat['size'])

luggage = {'combo': '12345', 'location': 'locker'}
print('combo')

birthdays = {'Lucas': '120892', 'Rose': '141091', 'mum': '160665'}

while True:
	print('Enter a name (blank to quit)')
	name = input()
	if name == "":
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have the birthday information for ' + name)
		print('What is their birthday')
		bday = input()
		birthdays[name] = bday
		print('birthday added to database')

spam = {'colour': 'red', 'age': '42'}

for i, j in spam.items():
	print(i + ' ' + str(j))

print(list(spam.keys()))
check = 'colour' in spam.keys()
print(check)

print(' I am ' + str(spam.get('colour', 'red')))

test = spam.setdefault('height', 'average')
print(test)
print(spam)
test2 = spam.setdefault('height', 'small')
print(test2)
print(spam)

import pprint
char = 'this is a message that will use set default and count'
count = {}
for i in char:
	count.setdefault(char, 0)
	count[char] = count[char] + 1
print(count)
pprint.pprint(count)