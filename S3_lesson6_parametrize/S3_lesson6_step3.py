import pytest
import time
import math


class TestLogin:
    @pytest.mark.parametrize('number_url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_guest_should_see_login_link(self, browser, number_url):
        link = f"https://stepik.org/lesson/{number_url}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        x = str(answer)
        browser.implicitly_wait(10)
        browser.find_element_by_class_name("string-quiz__textarea").send_keys(x)
        browser.find_element_by_class_name("submit-submission").click()
        # time.sleep(100)
        actual_result = browser.find_element_by_class_name("smart-hints__hint").text
        expected_result = "Correct!"
        assert actual_result == expected_result, f"Ошибка Ответа, фактический результат {actual_result}, а должен быть {expected_result}"
