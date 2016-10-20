
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


username =  "abzter"
access_key = "7150fcd6-f478-4b20-96fa-a405dc40e5ca"


test_environment_details = {
	'platform' : "OS X 10.11" ,
	'browsername' : "chrome" ,
	'version' : "53.0" ,
	'name' : "Testing the Slack Bot"
}

browser = webdriver.Remote(
	command_executor= 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'%(username , access_key), 
	desired_capabilities=test_environment_details
	)

#Test
browser.get("https://www.google.com")
search_input=browser.find_element_by_name("q")
search_input.send_keys("github")
search_input.submit()
time.sleep(2)
print(browser.title)
browser.quit()

