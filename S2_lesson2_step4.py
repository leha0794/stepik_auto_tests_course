from selenium import webdriver
browser = webdriver.Chrome()


# browser.execute_script("alert('Robots at work');")

# Обратите внимание, что исполняемый JavaScript нужно заключать в кавычки (двойные или одинарные).
# Если внутри скрипта вам также понадобится использовать кавычки,
# а для выделения скрипта вы уже используете двойные кавычки,
# то в скрипте следует поставить одинарные:

# browser.execute_script("document.title='Script executing';")

# Можно с помощью этого метода выполнить сразу несколько инструкций,
# перечислив их через точку с запятой.
# Изменим сначала заголовок страницы,
# а затем вызовем alert:

browser.execute_script("document.title='Script executing';alert('Robots at work');")