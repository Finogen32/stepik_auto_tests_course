from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Условие для нажатия кнопки (ищем ее по ID устанавливаем условие нажатия потом ищем саму кнопку и нажимаем на нее):
    button = WebDriverWait(browser,30).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.ID,'book')
    button.click()
    #Ищем значение для х:
    x_element = browser.find_element_by_css_selector('span#input_value')
    x = int(x_element.text)
    x = calc(x)
    #Ищем поле ввода и вставляем в него рассчетное значение:
    input = browser.find_element_by_css_selector('input#answer.form-control')
    input.send_keys(x)

    #Ищем кнопку и нажимаем на нее:
    button = browser.find_element_by_css_selector('button#solve.btn.btn-primary').click()

    
finally:
    time.sleep(5)
    browser.quit()
