from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print(x)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element_by_id("answer").send_keys(calc(x))
    chek1 = browser.find_element_by_id("robotCheckbox").click()
    chek2 = browser.find_element_by_css_selector("[value='robots']").click()
    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
