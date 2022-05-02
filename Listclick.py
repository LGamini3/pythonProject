from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID, "num1")
    b = browser.find_element(By.ID, "num2")
    n1 = int(a.text)
    n2 = int(b.text)
    sum = int(n1 + n2)
    #print(sum)
    sum2 = str(sum)
    #print(type(sum2))
    #print(sum2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(sum2))

    button = browser.find_element(By.XPATH,'//*[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

