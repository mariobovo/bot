from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(r"--user-data-dir=E:\jupyter\selenium")

#driver.get('https://web.whatsapp.com')  # Already authenticated
#time.sleep(5)
usernameStr = 'test'
passwordStr = 'test'
#browser = webdriver.Chrome()
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F')
#username = browser.find_element_by_id('yup5K8')
time.sleep(5)
username=browser.find_element_by_name("loginKey")
username.send_keys(usernameStr)
time.sleep(5)
password=browser.find_element_by_name("password")
password.send_keys(passwordStr)

#password = WebDriverWait(browser, 10).until(
#EC.presence_of_element_located((By.ID, 'Passwd')))
#password.send_keys(passwordStr)
time.sleep(5)
#signInButton = browser.find_elements_by_class_name('wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1')
#signInButton = browser.find_element(By.CLASS_NAME, "wyhvVD _1EApiB hq6WM5 L-VL8Q cepDQ1 _7w24N1")
#signInButton.click()
browser.find_element_by_xpath('//button[normalize-space()="Đăng nhập"]').click()