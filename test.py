from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_check_login_form():
    # TODO: Need to improve this test by disabling unnecessary loading of object on front end
    # Pre-condition: Open website via chrome browser and confirm your age
    driver = webdriver.Chrome()
    driver.get('https://csgorun.pro/')
    assert 'CSGORUN' in driver.title, 'Website was not opened'

    element = driver.find_element(by=By.CLASS_NAME, value="switcher__content")
    element.click()

    # Step 1. Open Steam login screen
    element = driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/header/div[2]/button[1]')
    element.click()
    sleep(5)  # TODO: find the way to get current state
    assert 'Steam' in driver.title, 'Transition to Steam login page does not appear'

    # Step 2.1 Insert invalid steam account
    element = driver.find_element(value="steamAccountName")
    element.clear()
    element.send_keys('wrong_test_account')

    # Step 3.2 Insert correct password
    element = driver.find_element(value="steamPassword")
    element.clear()
    element.send_keys('Qazwsx321')

    # Step 3.3 Press sign in button
    element = driver.find_element(By.XPATH, value='//*[@id="imageLogin"]')
    element.click()
    sleep(5)  # TODO: find the way to get current state
    assert 'name or password that you have entered is incorrect.' in driver.page_source, 'Message does not appear on screen'

    # Post condition: Close web browser
    driver.quit()
