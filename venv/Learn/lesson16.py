from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    start = browser.find_element(By.TAG_NAME, "button")
    start.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(3)
    x_element = browser.find_element(By.ID, "input_value").text
    x = x_element

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    # browser.find_element(By.ID, "robotCheckbox").click()
    # browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
