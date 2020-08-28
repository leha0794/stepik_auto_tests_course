class Test:

    def test_for_various_language(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(10)
        assert is_element_present(browser)==True, "корзинка не найдена"

def is_element_present(browser):
    try:
        browser.find_element_by_class_name("btn-add-to-basket")
        return True
    except:
        return False