import json
from csv_transformations import csv_to_list, json_to_csv
from batch_processor import loop_engine

if __name__ == "__main__":
    # Provide Input File Path
    output_file = "output_log.json"
    url_list = csv_to_list(file_path='input.csv')
    data_json = loop_engine(url_list, output_file, api_key='')
    print(json.dumps(data_json, indent=4))
    json_to_csv(data_json)