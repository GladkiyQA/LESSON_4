from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

BUTTON = ('xpath', '//button[@onclick="addElement()"]')

DELETE_BUTTON = ('xpath', './/button[@onclick="deleteElement()"]')

click_five_time = driver.find_element(*BUTTON)

for click in range(5):
    click_five_time.click()
delete_buttons = driver.find_elements(*DELETE_BUTTON)
print(len(delete_buttons))

driver.quit()
