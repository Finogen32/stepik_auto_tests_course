from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    box_element = browser.find_element_by_css_selector('img#treasure')
    box_checked = box_element.get_attribute("valuex")
    x = box_checked
    y = calc(x)
    input1 = browser.find_element_by_css_selector('input#answer')
    input1.send_keys(y)
    option1=browser.find_element_by_css_selector('input#robotCheckbox')
    option1.click()
    option2=browser.find_element_by_css_selector('input#robotsRule.check-input')
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()