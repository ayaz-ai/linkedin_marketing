from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def visit_company_page(driver):
    driver.find_element(By.CSS_SELECTOR,'[data-field="experience_company_logo"]').click()
    time.sleep(20)
    element = driver.find_element(By.CSS_SELECTOR, "h1.org-top-card-summary__title span[dir='ltr']")
    text = element.text
    print(text)
    about = driver.find_element(By.LINK_TEXT, 'About')
    about.click()
    time.sleep(20)
    return text

def scrap_about(driver):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    dl_element = soup.find('dl', class_='overflow-hidden')

    website = 'NULL'
    hq_phone = 'NULL'
    industry = 'NULL'
    company_size = 'NULL'
    headquaters = 'NULL'

    for dt_element, dd_element in zip(dl_element.find_all('dt'), dl_element.find_all('dd')):
        dt_text = dt_element.get_text(strip=True)
        dd_text = dd_element.get_text(strip=True)
        if dt_text == 'Website':
            print(f"{dt_text}: {dd_text}")
            website = dd_text
        if dt_text == 'Phone':
            # Find the first <span> within the <dd> element
            span_element = dd_element.find('span', attrs={'dir': 'ltr'})
            if span_element:
                phone_span = span_element.get_text(strip=True)
                print(f"{dt_text}: {phone_span}")
                hq_phone = phone_span 
            else:
                print(f"No <span> element with dir='ltr' found for {dt_text}.")
        if dt_text == 'Industry':
            print(f"{dt_text}: {dd_text}")
            industry = dd_text
        if dt_text == 'Company size':
            print(f"{dt_text}: {dd_text}")
            company_size = dd_text
        if dt_text == 'Founded':
            print(f"Headquaters: {dd_text}")
            headquaters = dd_text

    return [website, hq_phone, industry, company_size, headquaters]