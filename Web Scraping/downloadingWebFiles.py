#! python3
import requests

####################################################################################################
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

####################################################################################################
# An example of a non-existing webpage and how raise_for_status returns an error 
# res = requests.get('https://automatetheboringstuff.com/files/page_that_does_not_exist')
# res.raise_for_status()

# Use a try and except so if an unnsuccessful download occurs, the program doesnt end
# try:
# 	res.raise_for_status()
# except Exception as exc:		
# 	print(f'There was a problem with {exc}')

####################################################################################################
# Download and save files to the HDD
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RandJ.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()

####################################################################################################