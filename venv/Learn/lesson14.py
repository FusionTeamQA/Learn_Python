from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value").text
    x = x_element

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    print(y)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
