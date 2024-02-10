import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/entry_ad")

time.sleep(2) # Пока не прошли ожидания, будут таймслипы :)

ALERT_WINDOW_BUTTON = ('xpath', '//div[@class="modal-footer"]')

driver.find_element(*ALERT_WINDOW_BUTTON).click()

driver.quit()