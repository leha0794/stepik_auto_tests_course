from selenium import webdriver
import time
from  selenium.webdriver.support.ui import Select
try:
    link = "http://suninjuly.github.io/selects1.html"
    # с открытым списком http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text

    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    z = int(x) + int(y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(z))

    button = browser.find_element_by_class_name("btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()

