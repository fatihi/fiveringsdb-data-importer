import json
from database_controller import DatabaseController
from helper import *


class CycleImporter:
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Cycle.json"
        self.table_name = "cycle"
        columns = ["id", "name", "position", "size"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def execute_import(self):
        with open(self.packs_data_file, encoding="UTF-8") as cycles_json:
            cycles = json.load(cycles_json)
            values = []
            for cycle in cycles:
                cycle_values = "("
                cycle_values += "\'" + cycle["id"] + "\', "
                cycle_values += "\'" + cycle["name"] + "\', "
                cycle_values += str(cycle["position"]) + ", "
                cycle_values += str(cycle["size"])
                cycle_values += ")"
                values.append(cycle_values)
            values_string = ", ".join(values)
            self.database_controller.upsert(self.table_name, self.columns, values_string, self.key, self.update)
