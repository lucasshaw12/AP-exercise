from pathlib import Path
import re
import glob
import os

# open up all .txt files within /Users/Lucas and children dirs
findDir = Path('/Users/Lucas/')

searchedWord = input('\nEnter the word that you wish to find: ')

# loop through the generator that glob returns
for txtFiles in findDir.glob('*.txt'):
	openFile = open(txtFiles)
	readRtfFiles = openFile.read()
	fileName = os.path.basename(txtFiles)

	# use an input as a regex expression to find sample
	regex = re.compile(searchedWord)
	txtRegex = regex.findall(readRtfFiles)

	if not txtRegex:
		pass
	else:	
		print(f'These files have the string "{searchedWord}": "{fileName}"')


	
