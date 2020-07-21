import pyperclip as pyperclip
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

try:

    button = browser.find_element_by_class_name("btn.btn-primary").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_answer = browser.find_element_by_id("answer").send_keys(calc(x))

    button2 = browser.find_element_by_class_name("btn.btn-primary").click()

    alert = browser.switch_to.alert
    # Копируем текст
    alert_text = alert.text
    # Split возвращает список, в качестве разделителя используем 'двоеточие пробел',
    # берём последний элемент, это нужное нам число
    addToClipBoard = alert_text.split(': ')[-1]
    # Копируем в буфер обмен
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(100)
    browser.quit()
