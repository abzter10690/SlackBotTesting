
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


username =  os.environ.get('SAUCE_USERNAME')
access_key =  os.environ.get('SAUCE_ACCESS_KEY')

print(username)
print(access_key)

