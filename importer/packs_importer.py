import json
from database_controller import DatabaseController
from helper import *


class PacksImporter:
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Pack.json"
        self.table_name = "pack"
        columns = ["id", "name", "position", "released_at", "size", "cycle_id", "ffg_id"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def execute_import(self):
        with open(self.packs_data_file, encoding="UTF-8") as packs_json:
            packs = json.load(packs_json)
            values = []
            for pack in packs:
                value = "("
                value += "\'" + transform_string(pack["id"]) + "\', "
                value += "\'" + transform_string(pack["name"]) + "\', "
                value += str(pack["position"]) + ", "
                value += "\'" + pack["released_at"] + "\', "
                value += str(pack["size"]) + ", "
                value += "\'" + transform_string(pack["cycle_id"]) + "\', "
                value += "\'" + transform_string(pack["ffg_id"]) + "\'"
                value += ")"
                values.append(value)
            values_string = ", ".join(values)
            self.database_controller.upsert(self.table_name, self.columns, values_string, self.key, self.update)
