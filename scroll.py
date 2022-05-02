import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    y = browser.find_element(By.ID,"input_value")
    r = int(y.text)
    print(r)

    def calc(r):
        return str(math.log(abs(12*math.sin(r))))

    p = calc(r)
    print(p)

    browser.execute_script("window.scrollBy(0, 100);")
    input = browser.find_element(By.ID, "answer").send_keys(str(p))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.XPATH,'//*[text()="Submit"]').click()
    #input = browser.find_element(By.ID, 'answer').send_keys(str(y))
    #input.send_keys(y)

finally:
     time.sleep(10)
    # закрываем браузер после всех манипуляций
     browser.quit()

