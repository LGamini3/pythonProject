# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
import pickle

#chrome_options = Options()
#chrome_options.add_argument("user-data-dir=selenium")
#driver = webdriver.Chrome(chrome_options=chrome_options)
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

#driver = webdriver.Chrome(chrome_options=chrome_options)

options = webdriver.ChromeOptions()
options.add_argument("user-agent=uHello World")
driver = webdriver.Chrome(options=options)

#pikle.dump(driver.get_cookies(),open("coockies", "wb"))
#cookies = pickle.load(open("cookies.pkl", "rb"))
#for cookie in cookies:
  #  driver.add_cookie(cookie)
#pickle.dump( driver.get_cookies() ,
             #open("cookies.pkl","wb"))
#search_box = driver.find_element(By.NAME,"q")
#search_box.send_keys("webdriver")
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

try:
    driver.get("https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have")
    time.sleep(10)
except Exeption as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


