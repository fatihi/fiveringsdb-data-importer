import json
from database_controller import DatabaseController


class PacksImporter:
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Pack.json"
        self.table_name = "pack"
        self.columns = "id, name, position, released_at, size, cycle_id, ffg_id"

    def execute_import(self):
        with open(self.packs_data_file, encoding="UTF-8") as packs_json:
            packs = json.load(packs_json)
            for pack in packs:
                pass
