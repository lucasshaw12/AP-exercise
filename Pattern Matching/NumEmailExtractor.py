# Get the text off the clipboard 
# Find all phone numbers and emails within the text
# Paste them onto the clipboard
# Use the pyperclip module to copy and paste strings
# Created 2 regexes, 1 for matching phone numbers and the other for matching email addresses
# Find all matches, not just the first, for both regexes
# Neatly format the matches string into a single string to paste
# Display some kind of text if no matches were found

#! python3
# phone and email

import pyperclip, re

# Expression for finding phone number (US version)
phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)? # seperator
	(\d{3}) # first 3 digits
	(\s|-|\.) # seperator
	(\d{4}) # last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

# expression for matching an email address
email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ # username
	@ # @ symbol
	[a-zA-Z0-9.-]+ # domain name
	(\.[a-zA-Z]{2,4}) # dot something top level domain
	)''', re.VERBOSE
	)

# find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
	phone_num = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phone_num += ' x' + groups[8]
	matches.append(phone_num)
for groups in email_regex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard: ')
	print('\n'.join(matches))
else:
	('No numbers or email addresses found')


