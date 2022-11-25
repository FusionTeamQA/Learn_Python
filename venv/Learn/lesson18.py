from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, "book").click()
    x_element = browser.find_element(By.ID, "input_value").text
    x = x_element


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    # browser.find_element(By.ID, "robotCheckbox").click()
    # browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
