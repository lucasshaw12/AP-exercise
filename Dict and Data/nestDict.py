allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
			'Bob': {'sandwich': 3, 'pretzels': 2},
			'Carol': {'cups': 2, 'pies': 1}}

def totalBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought

print('Number of things being brought')
print(' - Apples' + str(totalBrought(allGuests, 'apples')))
print(' - Pretzels' + str(totalBrought(allGuests, 'pretzels')))
print(' - cakes' + str(totalBrought(allGuests, 'cakes')))
print(' - Cups' + str(totalBrought(allGuests, 'cups')))
print(' - Pies' + str(totalBrought(allGuests, 'pies')))

print(allGuests['Alice'], allGuests['Bob'])