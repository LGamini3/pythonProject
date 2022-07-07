from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(3)
    button = driver.find_element(By.XPATH, './/button[@class="btn btn-primary"]')
    button.click()
    alert = driver.switch_to.alert
    alert.accept()
    a = driver.find_element(By.ID, "input_value")
    f = int(a.text)
    print(f)
    def calc(f):
        return str(math.log(abs(12*math.sin(int(f)))))
    ans = calc(f)
    answer = driver.find_element(By.ID, "answer").send_keys(str(ans))
    driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
finally:
    time.sleep(30)
    driver.quit()


