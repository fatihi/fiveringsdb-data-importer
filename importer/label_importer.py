from database_controller import DatabaseController
from helper import *
from importer.importer_base import Importer


class LabelImporter(Importer):
    def __init__(self, data_folder_path):
        self.packs_data_file = data_folder_path + "Label/en.json"
        self.table_name = "label"
        columns = ["id", "value"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def get_value(self, entry):
        value = "("
        value += "\'" + transform_string(entry["id"]) + "\', "
        value += "\'" + transform_string(entry["value"]) + "\'"
        value += ")"
        return value
