import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    f_name = browser.find_element(By.NAME, "firstname")
    f_name.send_keys("123")
    l_name = browser.find_element(By.NAME, "lastname")
    l_name.send_keys("123")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("123")

    load = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    load.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()
    confirm = browser.switch_to.alert
    print(email)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)

    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
