import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.MacOS
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Команда для запуска тестов кторые имют маркеры smoke и MacOS (не обязательно одновременно)
# pytest -s -v -m "smoke or MacOS" S3_lesson5_step3.py
# Запустится два теста

# Команда для запуска тестов кторые имют одновременно маркеры smoke и MacOS
# pytest -s -v -m "smoke and MacOS" S3_lesson5_step3.py
# Запустится только второй тест

