import pyperclip as pyperclip
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:

    button = browser.find_element_by_class_name("trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input_answer = browser.find_element_by_id("answer").send_keys(calc(x))

    button2 = browser.find_element_by_class_name("btn.btn-primary").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    
finally:
    browser.quit()
