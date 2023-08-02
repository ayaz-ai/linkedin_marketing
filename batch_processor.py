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
    name, email = email_fetcher(url)
    data_dictionary[url]['email'] = email
    data_dictionary[url]['name'] = name
    return data_dictionary