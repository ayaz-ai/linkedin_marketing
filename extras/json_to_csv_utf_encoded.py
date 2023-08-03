import csv

def json_to_csv(data_json):
    with open('output.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['LinkedIn Profile URL', 'Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for url, data in data_json.items():
            url = url
            name = data['name']
            email = data['email']
            writer.writerow({'LinkedIn Profile URL': url, 'Name': name, 'Email': email})

