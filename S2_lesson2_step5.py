from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()

# Принудительно скролим страницу
button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# Эта команда проскроллит страницу на 100 пикселей вниз:
browser.execute_script("window.scrollBy(0, 100);")

button.click()



time.sleep(3)
browser.quit()
