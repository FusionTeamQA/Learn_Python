from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    print(x)
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.XPATH, "/html/body/div/form/button").click()

    # input1 = browser.find_element(By.TAG_NAME, "input")
    # input1.send_keys("Ivan")
    # input2 = browser.find_element(By.NAME, "last_name")
    # input2.send_keys("Petrov")
    # input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    # input3.send_keys("Smolensk")
    # input4 = browser.find_element(By.ID, "country")
    # input4.send_keys("Russia")
    # button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла