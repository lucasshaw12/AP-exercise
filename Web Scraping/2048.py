#! python3
# Play the 2048 game on https://gabrielecirulli.github.io/2048/ using automation

import webbrowser, time
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Navigate to website
# browser = webdriver.Chrome() # Opens Chrome using Selenium
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install()) # Opens Firefox using Selenium
url = 'https://gabrielecirulli.github.io/2048/'
browser.get(url)

# Navigate cookies popup
time.sleep(1)
linkElem = browser.find_element_by_id('ez-accept-all')
linkElem.click()

# input keypresses. Use 'html' tag as this is the base tag for websites
htmlElem = browser.find_element_by_tag_name('html')

# Create a loop to continously input keys until game has been won
while True:
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)

	try:
		retryElem = browser.find_element_by_link_text('Try again')
		retryElem.click()
	except:
		pass

	




