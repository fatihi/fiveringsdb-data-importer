import json
from database_controller import DatabaseController
from helper import *
from importer.importer_base import Importer


class CycleImporter(Importer):
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Cycle.json"
        self.table_name = "cycle"
        columns = ["id", "name", "position", "size"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    @staticmethod
    def get_value(entry):
        value = "("
        value += "\'" + transform_string(entry["id"]) + "\', "
        value += "\'" + transform_string(entry["name"]) + "\', "
        value += str(entry["position"]) + ", "
        value += str(entry["size"])
        value += ")"
        return value
