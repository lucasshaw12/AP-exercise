#! python3
# Visit a webpage, then attempt to download all links on that page. 
# Any links which are broken are to be displayed

import requests, os, bs4, re

# Create a new folder to download webpages to
os.makedirs('Downloaded Pages', exist_ok=True)

# Download webpage
url = 'https://www.python.org/'
res = requests.get(url)
res.raise_for_status() # Check if the download was successful

soupObj = bs4.BeautifulSoup(res.text, 'html.parser') # Collects all text form the webpage

# Find all 'a' links on the webpage
linkElem = soupObj.select('a')
numOfLinks = len(linkElem)

for i in range(numOfLinks):
	linkUrlToOpen = 'https://www.python.org' + linkElem[i].get('href')
	# print(os.path.basename(linkUrlToOpen))
	print(os.path.abspath('.//Downloaded Pages/' + linkUrlToOpen))

	filename = re.sub(r'[\/*:"?]+', '-', linkUrlToOpen.split("://")[1])
	downloadedPage = open(os.path.join('Downloaded Pages', filename), 'wb')

	if linkElem == []:
		print('Error, link does not work')
	else:
		for chunk in res.iter_content(100000):
			downloadedPage.write(chunk)
		downloadedPage.close()





