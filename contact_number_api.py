import requests
from json.decoder import JSONDecodeError

def contact_phone(url, key):
    api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-contact'
    api_key = key
    header_dic = {'Authorization': 'Bearer ' + api_key}
    params = {
        'linkedin_profile_url': url
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    
    try:
        response_data = response.json()
    except JSONDecodeError as e:
        # Handle the JSONDecodeError here (e.g., log the error, raise a custom exception, etc.)
        print(f"JSONDecodeError: {e}")
        response_data = {"numbers": []}  # Set a default value or return None in case of error
    
    return response_data