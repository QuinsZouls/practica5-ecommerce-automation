from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import os
import time

WITH_SIGN_UP = False


def sign_up_user(driver=webdriver.Chrome):
    signUpLink = driver.find_element(By.CSS_SELECTOR, '#signin2')
    signUpLink.click()
    time.sleep(1)
    userInput = driver.find_element(By.CSS_SELECTOR, '#sign-username')
    userInput.send_keys('ALFREDO')
    passwordInput = driver.find_element(By.CSS_SELECTOR, '#sign-password')
    passwordInput.send_keys('password')
    time.sleep(1)
    signBtn = driver.find_element(
        By.CSS_SELECTOR, '#signInModal > div > div > div.modal-footer > button.btn.btn-primary')
    signBtn.click()
    time.sleep(1)
    passwordInput.send_keys(Keys.ENTER)


def login(driver=webdriver.Chrome):
    loginLink = driver.find_element(By.CSS_SELECTOR, '#login2')
    loginLink.click()
    time.sleep(1)
    userInput = driver.find_element(By.CSS_SELECTOR, '#loginusername')
    userInput.send_keys('ALFREDO')
    passwordInput = driver.find_element(By.CSS_SELECTOR, '#loginpassword')
    passwordInput.send_keys('password')
    loginBtn = driver.find_element(
        By.CSS_SELECTOR, '#logInModal > div > div > div.modal-footer > button.btn.btn-primary')
    loginBtn.click()
    time.sleep(1)


def add_cart_items(driver=webdriver.Chrome):
    categories = driver.find_elements(By.CSS_SELECTOR, '#itemc')
    print(len(categories))
    for category in categories:
        category.click()
        time.sleep(1)
        items = driver.find_elements(By.CSS_SELECTOR, '#tbodyid > div')
        for i in range(2):
            link = items[i].find_element(
                By.CSS_SELECTOR, '#tbodyid > div:nth-child(%i) > div > div > h4 > a' % (i + 1))

            link.click()
            time.sleep(1)
            addToCartBtn = driver.find_element(
                By.CSS_SELECTOR, '#tbodyid > div.row > div > a')
            addToCartBtn.click()
            time.sleep(1)
            alert = driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            driver.back()
            driver.back()


# Optional argument, if not specified will search path.
driver = webdriver.Chrome(
    os.getenv('WEBDRIVER_PATH', '/Users/alfredomedrano/Development/tools/chromedriver'))

driver.get('https://www.demoblaze.com/index.html')

time.sleep(2)  # Let the user actually see something!

if WITH_SIGN_UP:
    sign_up_user(driver)
login(driver)
add_cart_items(driver)
driver.quit()
