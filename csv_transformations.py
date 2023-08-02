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

def write_output(data_dictionary):
    output_file = "output.csv"
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['LinkedIn Profile URL', 'Name', 'Numbers', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for url, data in data_dictionary.items():
            writer.writerow({'LinkedIn Profile URL': url, 'Name':['name'], 'Email': data['email']})