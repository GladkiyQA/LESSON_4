import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/entry_ad")

time.sleep(2) # Пока не прошли ожидания, будут таймслипы :)

ALERT_WINDOW_BUTTON = ('xpath', '//div[@class="modal-footer"]')

driver.find_element(*ALERT_WINDOW_BUTTON).click()