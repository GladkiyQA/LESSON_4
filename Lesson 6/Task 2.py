import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

driver.get('http://uitestingplayground.com/textinput')

INPUT_FIELD = ('xpath', '//input[@id="newButtonName"]')
BUTTON = ('xpath', '//button[@id="updatingButton"]')
special_text = "SkyPro"
text_input = driver.find_element(*INPUT_FIELD).send_keys(special_text)
button = driver.find_element(*BUTTON).click()
text_in_button = wait.until(EC.text_to_be_present_in_element(BUTTON, special_text))

print(driver.find_element(*BUTTON).text)