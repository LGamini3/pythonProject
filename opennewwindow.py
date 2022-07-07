from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(3)
    button = driver.find_element(By.XPATH, './/button[@class="trollface btn btn-primary"]')
    button.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    time.sleep(2)
    findx= driver.find_element(By.ID, "input_value")
    x = int(findx.text)
    print(x)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    ret = calc(x)
    answer = driver.find_element(By.ID, "answer").send_keys(str(ret))
    driver.find_element(By.XPATH,'//button[@class="btn btn-primary"]').click()
finally:
    time.sleep(30)
    driver.quit()




