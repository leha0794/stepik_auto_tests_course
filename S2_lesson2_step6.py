import math
from selenium import webdriver
import time

browser = webdriver.Chrome()
link = " http://SunInJuly.github.io/execute_script.html"
browser.get(link)
try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    browser.execute_script("window.scrollBy(0, 120);")
    input = browser.find_element_by_id("answer").send_keys(y)
    check = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']").click()
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
