import requests, bs4

#################################################################################
# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup)) 

# #################################################################################
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, 'lxml')
# print(type(exampleSoup))

#################################################################################
# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)

# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(str(pElems[1].getText()))
# print(str(pElems[2]))
# print(str(pElems[2].getText()))

#################################################################################
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexisting_address') == None)
print(spanElem.attrs)