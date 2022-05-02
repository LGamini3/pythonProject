from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мy answer")

    button = browser.find_element_by_xpath('//*[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()


