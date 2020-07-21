from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    first_name = browser.find_element_by_name("firstname").send_keys("тест")
    last_name = browser.find_element_by_name("lastname").send_keys("тест")
    email = browser.find_element_by_name("email").send_keys("test@test.test")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, "Test.txt")  # добавляем к этому пути имя файла
    select_file = browser.find_element_by_id("file").send_keys(file_path)

    # Путь к файлу
    print(os.path.abspath(__file__))
    # Путь до файла
    print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element_by_class_name("btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
