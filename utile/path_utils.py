import json
import os
def load_json_data(file_name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(BASE_DIR,"data",file_name)
    with open(json_path,"r",encoding="utf-8") as f:
        return json.load(f)
def get_pet_data():
    return load_json_data("pet_data.json")

def get_query_data():
    return load_json_data("get_pet_data.json")

def get_delete_data():
    return load_json_data("delete_pet_data.json")








