#! python3
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager # Adds geckodriver binary to path
import chromedriver_binary  # Adds chromedriver binary to path
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome() # Opens Chrome using Selenium
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install()) # Opens Firefox using Selenium
print(type(browser))



##############################################
# Finding the class, then return what element it belongs to

# browser.get('https://inventwithpython.com')
# try:
# 	elem = browser.find_element_by_class_name('card-img-top')
# 	print(f'Found {elem.tag_name} element with that class name!')

# except:
# 	print('Was not able to find an element with that class name.')

##############################################
# Clicking the page

# browser.get('https://inventwithpython.com')
# linkElem = browser.find_element_by_link_text('Read Online for Free')
# print(type(linkElem))
# linkElem.click() # Follows the read online for free link


##############################################
# Filling out and submitting forms
# browser.get('https://login.metafilter.com')
# userElem = browser.find_element_by_id('user_name')
# userElem.send_keys('your_real_username_here')

# passwordElem = browser.find_element_by_id('user_pass')
# passwordElem.send_keys('your_real_password_here')
# passwordElem.submit()

##############################################
# Sending special keys
# browser.get('https://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.HOME)





