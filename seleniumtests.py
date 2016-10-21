import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


username =  "abzter"
access_key = "7150fcd6-f478-4b20-96fa-a405dc40e5ca"


test_environment_details = {
	'platform' : "OS X 10.11" ,
	'browsername' : "chrome" ,
	'version' : "53.0" ,
	'name' : "seleniumtests.py"
}


test_environment_details = {
	'platform' : "OS X 10.11" ,
	'browsername' : "chrome" ,
	'version' : "53.0" ,
	'name' : "Testing the Slack Bot : tests.py"
}


inputCommands = [
      "@vmbot create box precise32 with pip install selenium, mkdir myproject",      
      "@vmbot Deploy precise32",
      "@vmbot Status processes python",
      "@vmbot Status health"
]

outputPassCommands = [
    "A vagrant box for ubuntu-precise32 has been created. Installed python. Installed selenium. Directory myproject created.\n\nBox now ready to be deployed."    
  ]

outputFailCommands = [
    "Failed to create precise32. A box with this name has already been created.",
    "Failed to deploy precise32.",
    "Failed to identify process python.",
    "Failed to obtain health."
  ]

browser = webdriver.Remote(
	command_executor= 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub'%(username , access_key), 
	desired_capabilities=test_environment_details
	)


browser.maximize_window()
wait = WebDriverWait(browser, 30)
browser.get("https://serverbot-project.slack.com/")
wait.until(EC.visibility_of_element_located((By.ID, "signin_btn"))) 

email= browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
email.send_keys("agrawal.akash22@gmail.com");
password.send_keys("Blahjohnsnow@2208");

signin = browser.find_element_by_id("signin_btn")
signin.click()

wait.until(EC.title_contains("general"))

browser.get("https://serverbot-project.slack.com/messages/serverbot")
wait.until(EC.title_contains("serverbot"))

messagebot = browser.find_element_by_id("message-input")
messagebot.send_keys(inputCommands[0]);
messagebot.send_keys(Keys.RETURN);

time.sleep(5)

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='msgs_div']/div[last()]/div[@class='day_msgs']/ts-message[last()]/div[@class='message_content ']/span[@class='message_body']")))
msg = browser.find_element_by_xpath("//div[@id='msgs_div']/div[last()]/div[@class='day_msgs']/ts-message[last()]/div[@class='message_content ']/span[@class='message_body']")

message = msg.text
print(message)

browser.quit()

'''
parts = message.split(":")
if parts[1].strip() == outputPassCommands[0]:
  unittest.assertEqual(outputPassCommands[0], parts[1].strip())
else:
  unittest.assertEqual(outputFailCommands[0], parts[1].strip())    
'''

'''

#Test
browser.get("https://www.google.com")
search_input=browser.find_element_by_name("q")
search_input.send_keys("github")
search_input.submit()
time.sleep(2)
print(browser.title)
browser.quit()

'''