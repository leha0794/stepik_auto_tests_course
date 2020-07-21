from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    # Проверяем наличие аттрибута checked для radiobuttons
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")

    # Первый вид проверки
    print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    # Второй способ ?
    assert people_checked == "true", "People radio is not selected by default"

    # Проверяем вторую кнопку
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("robots of people radio: ", robots_checked)
    assert robots_checked is not None, "Robots radio is not selected by default"


    input1 = browser.find_element_by_id("answer").send_keys(y)
    chek1 = browser.find_element_by_id("robotCheckbox").click()
    chek2 = browser.find_element_by_css_selector("[value='robots']").click()
    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
