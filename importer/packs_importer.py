from database_controller import DatabaseController
from helper import *
from importer.importer_base import Importer


class PackImporter(Importer):
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Pack.json"
        self.table_name = "pack"
        columns = ["id", "name", "position", "released_at", "size", "cycle_id", "ffg_id"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def get_value(self, entry):
        value = "("
        value += "\'" + transform_string(entry["id"]) + "\', "
        value += "\'" + transform_string(entry["name"]) + "\', "
        value += str(entry["position"]) + ", "
        released_at = 'NULL' if entry["released_at"] is None else "\'" + entry["released_at"] + "\'"
        value += released_at + ", "
        value += str(entry["size"]) + ", "
        value += "\'" + transform_string(entry["cycle_id"]) + "\', "
        value += "\'" + transform_string(entry["ffg_id"]) + "\'"
        value += ")"
        return value
