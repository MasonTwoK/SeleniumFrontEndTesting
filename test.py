from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO: Need to improve this test by disabling unnecessary loading of object on front end
# Step 1. Open website via chrome browser
driver = webdriver.Chrome()
driver.get('https://csgorun.pro/')
assert 'CSGORUN' in driver.title, 'Website was not opened'

# Step 2. Confirm your age
element = driver.find_element(by=By.CLASS_NAME, value="switcher__content")
element.click()

# Step 3. Open Steam login screen
element = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/header/div[2]/button[1]')
element.click()
sleep(5)  # TODO: find the way to get current state
assert 'Steam' in driver.title, 'Transition to Steam login page does not appear'

# Step 4.1 Insert invalid steam account
element = driver.find_element(value="steamAccountName")
element.clear()
element.send_keys('wrong_test_account')

# Step 4.2 Insert correct password
element = driver.find_element(value="steamPassword")
element.clear()
element.send_keys('Qazwsx321')

# Step 4.3 Press sign in button
element = driver.find_element(By.XPATH, value='//*[@id="imageLogin"]')
element.click()
sleep(5)  # TODO: find the way to get current state

response_data = driver.find_element(value="error_display")
assert response_data['text'] == 'The account name or password that you have entered is incorrect.'

# driver.quit()
