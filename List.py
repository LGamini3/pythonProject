from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    a = browser.find_element(By.ID, "num1")
    b = browser.find_element(By.ID, "num2")
    с = str(int(a) + int(b))
    #c = sum(int(a) + int(b))

    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.XPATH, "//option[@value = c ]").click()

    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(c)

    button = browser.find_element(By.XPATH,'//*[text()="Submit"]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()
