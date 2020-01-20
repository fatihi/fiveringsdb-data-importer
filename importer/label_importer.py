import json
from database_controller import DatabaseController
from helper import *


class LabelImporter:
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Label/en.json"
        self.table_name = "label"
        columns = ["id", "value"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def execute_import(self):
        with open(self.packs_data_file, encoding="UTF-8") as labels_json:
            labels = json.load(labels_json)
            values = []
            for label in labels:
                value = "("
                value += "\'" + transform_string(label["id"]) + "\', "
                value += "\'" + transform_string(label["value"]) + "\'"
                value += ")"
                values.append(value)
            values_string = ", ".join(values)
            self.database_controller.upsert(self.table_name, self.columns, values_string, self.key, self.update)
