#! python3
# Stopwatch program

import time
# Display the programs instructions
print('Press "ENTER" to begin. Press "ENTER" to click the stopwatch. Press "Ctrl-C" to quit')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Track the lap times
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time

except KeyboardInterrupt:
	# Handle the Ctrl-C exeptions to keep its error message from displaying.
	print('\nDone.')
