from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Заполняем все поля:
    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys("Imya")
    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys("Familiya")
    input2 = browser.find_element_by_css_selector('input[name="email"]')
    input2.send_keys("Email@gmail.com")
    #Пытаемся скинуть файл+ищем кнопку. В данном случает файл скидывается при помощи дирректории, но не через метод поиска: 
    #element = browser.find_element_by_css_selector('input[type=file]')
    #element.send_keys('G://Project//environments//test.txt')

    #ниже пример, в котором мы ищем деррикторию исполняемого файла и закдываем нужный файл (необходимый для задания):
    current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8.py'))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')                       # добавляем к этому пути имя файла 
    element = browser.find_element_by_css_selector('input[type=file]')
    element.send_keys(file_path)
    
    #Кликаем клавишу:
    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(5)
    browser.quit()
