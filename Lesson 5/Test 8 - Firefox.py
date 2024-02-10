import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/login")

USERNAME_FIELD = ('xpath', '//input[@id="username"]')
PASSWORD_FIELD = ('xpath', '//input[@id="password"]')
LOGIN_BUTTON = ('xpath', '//button[@type="submit"]')

user = driver.find_element(*USERNAME_FIELD).send_keys("tomsmith")
passwrd = driver.find_element(*PASSWORD_FIELD).send_keys("SuperSecretPassword!")
butt = driver.find_element(*LOGIN_BUTTON).click()

driver.quit()