from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://csgorun.pro/')
assert 'CSGORUN' in driver.title

age_confirmation_switch = driver.find_element(by=By.CLASS_NAME, value="switcher__content")
age_confirmation_switch.click()


