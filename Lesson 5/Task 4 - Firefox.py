from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

def click_dynamic_button():
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element('xpath', '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

for three_times in range(3):
    click_dynamic_button()
    driver.refresh()

driver.quit()