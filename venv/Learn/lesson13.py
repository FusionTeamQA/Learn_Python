from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1").text
    y_element = browser.find_element(By.ID, "num2").text
    x = x_element
    y = y_element


    def calc(x):
        return str(int(x) + int(y))


    z = calc(x)
    print(z)

    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select.select_by_visible_text(z) #Проверка что он есть
    select.select_by_value(str(z))
    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
