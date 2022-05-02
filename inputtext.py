from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #input1 = browser.find_element_by_tag_name("input")
    input1 = browser.find_element(By.Tag_Name, "input")
    input1.send_keys("Ivan")
    #input2 = browser.find_element_by_name("last_name")
    input2 = browser.find_element(By.Name,("last_name")
    input2.send_keys("Petrov")
    #input3 = browser.find_element_by_class_name("form-control.city")
    input3 = browser.find_element(By.Class_Name, "form-control.city")
    input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    input4 = browser.find_element(By.ID,"country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # wait for
    time.sleep(30)
    # close browser after all actions
    browser.quit()

