from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

driver.get('http://uitestingplayground.com/ajax')

BUTTON = ('xpath', '//button[@id="ajaxButton"]')
GREEN_FIELD = ('xpath', '//p[@class="bg-success"]')

click_to_button = driver.find_element(*BUTTON).click()
wait.until(EC.visibility_of_element_located(GREEN_FIELD))
green_text = driver.find_element(*GREEN_FIELD)


print(green_text.text)