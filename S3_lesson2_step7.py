from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"
browser.get(link)

try:

    actual_result = browser.find_element_by_tag_name("h1").text
    expected_result = "Hello1!"
    assert actual_result == expected_result, \
        f"Ошибка приветствия, фактический результат '{actual_result}', а должен быть '{expected_result}'"

finally:
    browser.quit()
