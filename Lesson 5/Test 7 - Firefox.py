import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/inputs")

INPUT_FIELD = ('xpath', '//input[@type="number"]')

driver.find_element(*INPUT_FIELD).send_keys("1000")
driver.find_element(*INPUT_FIELD).clear()
driver.find_element(*INPUT_FIELD).send_keys("999")

driver.quit()