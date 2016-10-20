import unittest
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

class SlackBotTesting(unittest.TestCase):

  def setUp(self):
      self.browser = webdriver.Remote(
	command_executor= 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'%(username , access_key), 
	desired_capabilities=test_environment_details
	)

  def test_search_in_google(self):
    browser = self.browser
    browser.maximize_window()
    browser.get("https://www.google.com")
    self.assertIn("Google", browser.title)
    search_input=browser.find_element_by_name("q")
    search_input.send_keys("github")
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)
    print(browser.title)

  def tearDown(self):
      self.browser.close()

if __name__ == "__main__":
	unittest.main()



