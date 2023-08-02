import json
from csv_transformations import csv_to_list 
from batch_processor import loop_engine

if __name__ == "__main__":
    # Provide Input File Path
    url_list = csv_to_list(file_path='input.csv')
    data_json = loop_engine(url_list, api_key='')
    print(json.dumps(data_json, indent=4))