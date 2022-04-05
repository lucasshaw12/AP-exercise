import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
	logging.debug('Start of game')
	print('Guess the coin toss, either heads or tails')
	guess = input()
	toss = random.randint(0, 1) # 0 is tails, 1 is heads

	logging.debug(f'Toss is {toss}')
	# assert toss == str, 'Toss value should be a string rather than an int: "' + str(toss) + '".'

if toss == guess:
	print('You got it')
	logging.debug(f'Toss is {toss}')
else:
	print('Nope! Guess again!')
	guess = input()
	logging.debug(f'Toss is {toss}')

	if toss == guess:
		print('You got it')
	else:
		print('Nope you are really bad at this game')

logging.debug('End of game')

# Toss is an int rather than 'heads' or 'tails'.
