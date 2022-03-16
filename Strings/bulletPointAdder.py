#! python 3
# bulletPointAdder.py # Adds wikipedia bullet points to the start of each line of text

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes of the line list
	lines[i] = '* ' + lines[i] # add star to each string in lines list

text = '\n'.join(lines)

pyperclip.copy(text)

# How to use
# Copy some text to the clipboard (Ctrl + C) or right click 'copy'.
# Run this script
# Then paste the text - it should now have a '*' appended to the start of the line



