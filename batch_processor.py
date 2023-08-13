from contact_number_api import contact_phone
from selenium_driver import email_fetcher

data_dictionary = {}

def loop_engine(url_list, api_key):
    
    for url in url_list:
        if url not in data_dictionary:
            data_dictionary[url] = {}
        # contact_api_hit(url, api_key)
        web_selenium(url)

    return data_dictionary

def contact_api_hit(url, key):
    contact = contact_phone(url, key)
    data_dictionary[url]['number'] = contact['numbers']
    return data_dictionary

def web_selenium(url):
    name, email, title, company_name, website, hq_phone, industry, company_size, headquaters = email_fetcher(url)
    data_dictionary[url]['email'] = email
    data_dictionary[url]['name'] = name
    data_dictionary[url]['title'] = title
    data_dictionary[url]['company_name'] = company_name
    data_dictionary[url]['website'] = website
    data_dictionary[url]['hq_phone'] = hq_phone
    data_dictionary[url]['industry'] = industry
    data_dictionary[url]['company_size'] = company_size
    data_dictionary[url]['headquaters'] = headquaters
    return data_dictionary