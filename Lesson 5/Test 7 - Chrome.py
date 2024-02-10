import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/inputs")

INPUT_FIELD = ('xpath', '//input[@type="number"]')

driver.find_element(*INPUT_FIELD).send_keys("1000")
driver.find_element(*INPUT_FIELD).clear()
driver.find_element(*INPUT_FIELD).send_keys("999")



