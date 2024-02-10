from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def click_dynamic_button():
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element('xpath', '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

for three_times in range(3):
    click_dynamic_button()
    driver.refresh()
