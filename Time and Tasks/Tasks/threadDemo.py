#! python3

import time, datetime, threading


# startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < startTime:
# 	time.sleep(1)
# print('Program now starting on Halloween 2029')

#######################################
# Multi-threading

print('Start of program')
def takeANap():
	time.sleep(5)
	print('Wake Up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')