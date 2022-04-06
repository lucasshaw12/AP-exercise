#! python3
# Syntax of the code to run = 'python commandLineEmailer.py [emailAddress] [userPassword] [email content]'

import webbrowser, sys, pyperclip, time
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

# Take an email address and string of text from the command line
if len(sys.argv) > 1:
	# Get address from command line
	emailAddress = ' '.join(sys.argv[1:2])
else: # Get address from clipboard
	emailAddress = pyperclip.paste()

if len(sys.argv) > 2:
	userPassword = ' '.join(sys.argv[2:3])
else:	
	userPassword = pyperclip.paste()

if len(sys.argv) > 3:
	emailContent = ' '.join(sys.argv[3:])
else:
	emailContent = pyperclip.paste()

# Log into email account shaw51@hotmail.co.uk
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://outlook.live.com/')
linkElem = browser.find_element_by_link_text('Sign in')
linkElem.click()

#Username
time.sleep(1)
linkElem = browser.find_element(By.ID, 'i0116')
linkElem.send_keys(emailAddress) # This will be the stored username from the terminal
# linkElem.send_keys('Lucaspython@hotmail.com') # manually enter the username
linkElem = browser.find_element_by_id('idSIButton9')
linkElem.click()

#Password
time.sleep(1)
linkElem = browser.find_element_by_id('i0118')
# linkElem.send_keys('Lucas-python-1') # Add password when running test
linkElem.send_keys(userPassword) # This will be stored from the argument within the termina
linkElem = browser.find_element_by_id('idSIButton9')
linkElem.click()

# 'Stay signed in' prompt
time.sleep(1)
linkElem = browser.find_element_by_id('idBtn_Back')
if linkElem.is_displayed() == True:
	linkElem.click()
else:
	pass

# New message
time.sleep(4)
linkElem = browser.find_elements_by_class_name('ms-Button-label')[1]
linkElem.click()

# Add recipient
time.sleep(4)
linkElem = browser.find_element_by_class_name('ms-BasePicker-input')
linkElem.click()
linkElem.send_keys(emailAddress)

# Add content
linkElem = browser.find_element_by_class_name('dbf5IpsJrfoz_ON4IquS')
linkElem.click()
# linkElem.send_keys('Hello automation test') 
linkElem.send_keys(emailContent) # This will be stored from the argument within the terminal or from copied text
time.sleep(1)

# Find the send button
linkElem = browser.find_elements_by_class_name('ms-Button--primary')[0]
linkElem.click()	

# Send without subject prompt
linkElem = browser.find_element_by_id('ok-1')
linkElem.click()

time.sleep(2)
browser.close()
