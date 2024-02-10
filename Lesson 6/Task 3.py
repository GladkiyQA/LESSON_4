import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

IMAGINE = ('xpath', '//img[@id="landscape"]')

wait.until(EC.visibility_of_element_located(IMAGINE))

third_imagine = driver.find_elements('xpath', '//img[@id]')[2].get_attribute("src")
print(third_imagine)

# У меня возникли проблемы с этим заданием. Я понимаю в чем ошибка, но не понимаю, как ее исправить
# Суть в том, что в начале я делал ожидание visibility_of_all_element_located. Но код завершался,
# как только селениум находил самый первый элемент, код не дожидался всех элементов.
# Поэтому, мне пришлось писать костыль, дожидаться последнего элемента появившегося, и потом уже искать третий.





