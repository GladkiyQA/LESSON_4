import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

def click_blue_button():
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element('xpath', '//button[contains(@class, "btn-primary")]')
    blue_button.click()
    time.sleep(2) # Это чтоб успеть нажать ОК во всплывающем окне.
    # Я знаю, что это делается иначе, но на этом уровне, пусть будет так :)

for three_times in range(3):
    click_blue_button()

driver.quit()