import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.exceptions import ProtocolError

desired_caps = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'DemoApp',
    'app': r'C:/Users/Abdallah/PycharmProjects/AppiumProject2/Base/calculator.apk',
    'appPackage': 'com.google.android.calculator',
    'appActivity': 'com.android.calculator2.Calculator'
}

try:
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
except ProtocolError as e:
    raise ProtocolError("Connection aborted.") from e

wait = WebDriverWait(driver, 20)
button_7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='11']")))
button_7.click()
multiply_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='14']")))
multiply_button.click()
button_9 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='13']")))
button_9.click()
left_parenthesis_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='8']")))
left_parenthesis_button.click()
button_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='19']")))
button_1.click()
button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='20']")))
button_2.click()
button_8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='12']")))
button_8.click()
divide_button =  wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='10']")))
divide_button.click()
button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='20']")))
button_2.click()
right_parenthesis_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='8']")))
right_parenthesis_button.click()
minus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='18']")))
minus_button.click()
button_4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='15']")))
button_4.click()
equals_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ImageButton[@index='26']")))
equals_button.click()
time.sleep(6)