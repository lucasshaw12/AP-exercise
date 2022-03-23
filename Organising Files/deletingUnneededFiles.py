import os, pyinputplus as pyip

inputFileSize = pyip.inputNum('Select minimum file size: ')

# walk through a folder tree 
for foldername, subfolders, filenames in os.walk('/Users/Lucas/Python'):
	for filename in filenames:
		fileSize = os.path.getsize(os.path.join(foldername, filename))
		
		if fileSize > inputFileSize: 
			print(f'Filename: {os.path.abspath(filename)} - File Size: {fileSize}')
