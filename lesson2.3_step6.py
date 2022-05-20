from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #кликаем кнопку:
    button = browser.find_element_by_css_selector('button.btn').click()
    #Переключаемся на новое окно + даем всем окнам имена:
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    #Ищем значение для х:
    x_element = browser.find_element_by_css_selector('span#input_value')
    x = int(x_element.text)
    x = calc(x)
    #Ищем поле ввода и вставляем в него рассчетное значение:
    input = browser.find_element_by_css_selector('input#answer.form-control')
    input.send_keys(x)

    #Ищем кнопку и нажимаем на нее:
    button = browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(3)
    browser.quit()