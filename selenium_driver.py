from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

def create_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument(r"--user-data-dir=C:\\Users\\ayazr\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(r'--profile-directory=Default')
    driver = webdriver.Chrome(options=options)
    return driver

def visit_profile(driver, link):
    profile_url = link
    driver.get(profile_url)
    time.sleep(50)
    class_name = 'text-heading-xlarge inline t-24 v-align-middle break-words'
    element = driver.find_element(By.XPATH, f"//*[contains(@class, '{class_name}')]")
    text = element.text
    print(text)
    return text


def check_email_element(driver):
    try:
        driver.find_element(By.CLASS_NAME, "x_LQDkG")
        return 'email_btn'
    except NoSuchElementException:
        pass
    
    try:
        driver.find_element(By.CLASS_NAME, "x_GxQlI")
        return 'email_revelied'
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.CLASS_NAME, "x_cGhxx")
        return 'no_email'
    except NoSuchElementException:
        pass
    return False

def email_resolver(driver):
    time.sleep(20)
    element = check_email_element(driver)
    if element == 'email_btn':
        email_revealer(driver)
        return email_resolver(driver)
    elif element == 'email_revelied':
        text_content = get_business_email(driver)
        return text_content
    elif element == 'no_email':
        return 'No Email'
    else:
        return'No Email'

def email_revealer(driver):
    driver.find_element(By.CLASS_NAME, "x_LQDkG").click()
    driver.refresh()
    return driver
    
def get_business_email(driver):
    element = driver.find_element(By.CLASS_NAME, "x_GxQlI")
    text_content = element.text
    return text_content

def email_fetcher(url):
    driver = create_driver()
    name = visit_profile(driver, url)
    email = email_resolver(driver)
    driver.quit()
    return [name, email]