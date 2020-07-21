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
    input1 = browser.find_element_by_id("answer").send_keys(y)
    chek1 = browser.find_element_by_id("robotCheckbox").click()
    # Использую css_selector для примера
    chek2 = browser.find_element_by_css_selector("[value='robots']").click()

    # Проверяем наличие аттрибута checked для radiobuttons


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
