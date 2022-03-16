# def isPhoneNumber(text):
# 	if len(text) != 12:
# 		return False

# 	for i in range(0, 3):
# 		if not text[i].isdecimal():
# 			return False

# 	if text[3] != '-':
# 		return False

# 	for i in range(4, 7):
# 		if not text[i].isdecimal():
# 			return False

# 	if text[7] != '-':
# 		return False

# 	for i in range(8, 12):
# 		if not text[i].isdecimal():
# 			return False

# 	return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
# for i in range(len(message)):
# 	chunk = message[i:i+12]
# 	if isPhoneNumber(chunk):
# 		print('Phone number found: ' + chunk)
# print('Done')

##################################################
###### THIS DOES THE SAME AS THE ABOVE ###########
import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print('Phone number found: ', mo.group())

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo1 = phoneNumRegex.search('My number is 415-555-4242')
# print('Phone number found: ', mo1.groups())

# area_code, main_num = mo1.groups()
# print(area_code + '-' + main_num)

# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo2 = phoneNumRegex.search('My number is (415) 555-4242')
# print('Phone number found: ', mo2.group(1), mo2.group(2))

##################################################
###### Matching using PIPE | ###########

# hero_regex = re.compile(r'Batman|Tina Fey')
# mo1 = hero_regex.search('Batman and Tina Fey')
# print(mo1.group())

# hero_regex = re.compile(r'Tina Fey|Batman')
# mo2 = hero_regex.search('Tina Fey and Batman')
# print(mo2.group())

##################################################
###### Matching using ?, + and * ###########

# bat_regex = re.compile(r'Bat(wo)?man')
# mo1 = bat_regex.search('The Adventures of Batman')
# print(mo1.group())

# bat_regex = re.compile(r'Bat(wo)*man')
# mo1 = bat_regex.search('The Adventures of Batman')
# print(mo1.group())

# # bat_regex = re.compile(r'Bat(wo)+man')
# # mo1 = bat_regex.search('The Adventures of Batman')
# # print(mo1.group())

# mo2 = bat_regex.search('The Adventures of Batwoman')
# print(mo2.group())

# mo3 = bat_regex.search('The Adventures of Batwowowowoman')
# print(mo3.group())

# mo4 = bat_regex.search('The Adventures of Batman')

#############################################################
###### Matching - Greedy or Non Greedy with {} and ? ########

# ha_regex = re.compile(r'(Ha){3}')
# mo1 = ha_regex.search('HaHaHa')
# print(mo1.group())

# mo2 = ha_regex.search('Ha')
# print(mo2 == None)

##################################################
###### Matching repetitions with {num1, num2} ####

# greedy_ha_regex = re.compile(r'(Ha){3,5}')
# mo1 = greedy_ha_regex.search('HaHaHaHaHa')
# print(mo1.group())

# non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
# mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
# print(mo2.group())

##################################################
###### Matching repetitions with finall() ################

# phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo1 = phone_number_regex.search('Cell: 415-555-9999 Work 202-555-0000')
# print(mo1.group())

# phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # No groups within this expression
# mo2 = phone_number_regex.findall('Cell: 415-555-9999 Work 202-555-0000')
# print(mo2)

# phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo3 = phone_number_regex.findall('Cell: 415-555-9999 Work 202-555-0000')
# print(mo3)

##################################################
######## Matching using charcter classes #########

# xmas_regex = re.compile(r'\d+\s\w+')
# mo1 = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo1)

##################################################
######## Matching using own custom classes using [] #########

# vowel_regex = re.compile(r'[aeiouAEIOU]')
# mo1 = vowel_regex.findall('RoboCop eats babyfood, BABYFOOD')
# print(mo1)

# consanont_regex = re.compile('[^aeiouAEIOU]')
# mo2 = consanont_regex.findall('RoboCop eats baby food, BABY FOOD')
# print(mo2)

##################################################
######## Matching using  Caret ^ and Dollar sign $ #########

# begins_with_hello = re.compile(r'^Hello')
# mo1 = begins_with_hello.search('Hello World')
# print(mo1)
# begins_with_hello.search('He said Hello') == None
# mo2 = begins_with_hello
# print(mo2)

# ends_with_number = re.compile(r'\d$')
# mo3 = ends_with_number.search('Your number is 42')
# print(mo3)

# whole_string_with_number = re.compile(r'^\d+$')
# mo4 = whole_string_with_number.search('1234567890')
# print(mo4)

##################################################
######## Matching using wildcard . ignores newlines \n ######### 

# at_regex = re.compile(r'.at')
# mo1 = at_regex.findall('The cat in the hat sat on the flat mat')
# print(mo1)

# name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo2 = name_regex.search('First Name: Lucas Last Name: Shaw')
# print(mo2.group())

# non_greedy_regex = re.compile(r'<.*?>')
# mo3 = non_greedy_regex.search('<To serve man> for dinner.>')
# print(mo3.group())

# greedy_regex = re.compile(r'<.*>')
# mo4 = greedy_regex.search('<To serve man> for dinner.>')
# print(mo4.group())


##################################################
######## Matching newlines with . includes newlines \n #########

# no_new_line_regex = re.compile(r'.*')
# print(no_new_line_regex.search('Serve the public trust.\nProtext the innocent.\nUphold the law.').group())

# new_line_regex = re.compile(r'.*', re.DOTALL)
# print(new_line_regex.search('Serve the public trust.\nProtext the innocent.\nUphold the law.').group())

##################################################
######## Case sensitive matching #########

# robocop = re.compile(r'robocop', re.I)
# mo1 = robocop.search('RoboCop is part man, part machine, all cop.')
# print(mo1.group())

# mo2 = robocop.search('ROBOCOP protects the innocent.')
# print(mo2.group())

# mo3 = robocop.search('Why does your programming book talk about robocop so much?')
# print(mo3.group())

##################################################
######## Substituting strings with the sub() method #########

# sub_regex = re.compile(r'Agent \w+')
# mo1 = sub_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# print(mo1)

# agent_names_regex = re.compile(r'Agewt (\w)\w*')
# mo2 = agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew that Agent Bob was a double agent')
# print(mo2)

##################################################
######## Complex Regexes using re.VERBOSE #########

# phone_regex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

### Or the better re.VERBOSE way

# phone_regex = re.compile(r'''(
# 	(\d{3}|\(\d{3}\))? # area code
# 	(\s|-|\.)? # seperator
# 	(\d{3}) # first 3 digits
# 	(\s|-|\.) # seperator
# 	(\d{4}) # last 4 digits
# 	(\s*(ext|x|ext.)\s*(\d{2,5}))?
# 	)''', re.VERBOSE)

##################################################
######## Combining re.IGNORECASE, re.DOTALL, re.VERBOSE using | (bitwise) #########

# some_regex_value = re.compile(r'foo', re.IGNORECASE | re.DOTALL)

# another_regex_value = re.compile(r'foo', e.IGNORECASE | re.DOTALL | re.VERBOSE)



























