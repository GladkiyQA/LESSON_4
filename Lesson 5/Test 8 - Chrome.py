import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

USERNAME_FIELD = ('xpath', '//input[@id="username"]')
PASSWORD_FIELD = ('xpath', '//input[@id="password"]')
LOGIN_BUTTON = ('xpath', '//button[@type="submit"]')

user = driver.find_element(*USERNAME_FIELD).send_keys("tomsmith")
passwrd = driver.find_element(*PASSWORD_FIELD).send_keys("SuperSecretPassword!")
butt = driver.find_element(*LOGIN_BUTTON).click()
