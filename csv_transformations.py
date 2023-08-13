import csv

def csv_to_list(file_path):
    url_list = []
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                url_list.append(row[0])
        # print(url_list)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

    return url_list

def json_to_csv(data_dictionary):
    output_file = "output.csv"
    with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['LinkedIn Profile URL', 'Name', 'Numbers', 'Email', 'Title', 'Company', 'Website', 'HQ Phone', 'Industry', 'Company Size', 'Headquaters']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for url, data in data_dictionary.items():
            writer.writerow({'LinkedIn Profile URL': url, 'Name':data['name'], 'Email': data['email'], 'Title': data['title'], 'Company': data['company_name'], 'Website': data['website'], 'HQ Phone': data['hq_phone'], 'Industry': data['industry'], 'Company Size': data['company_size'], 'Headquaters': data['headquaters']})