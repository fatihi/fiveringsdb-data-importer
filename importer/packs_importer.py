from database_controller import DatabaseController
from helper import *
from importer.importer_base import Importer


class PackImporter(Importer):
    def __init__(self, data_folder_path):
        self.data_file = data_folder_path + "Pack.json"
        self.table_name = "pack"
        columns = ["id", "name", "position", "released_at", "size", "cycle_id", "ffg_id"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def get_value(self, entry):
        value = "("
        value += "\'" + transform_string(entry["id"]) + "\', "
        value += get_nullable_string_value(entry, "name") + ", "
        value += get_nullable_number_value(entry, "position") + ", "
        value += get_nullable_string_value(entry, "released_at") + ", "
        value += get_nullable_number_value(entry, "size") + ", "
        value += "\'" + transform_string(entry["cycle_id"]) + "\', "
        value += get_nullable_string_value(entry, "ffg_id")
        value += ")"
        return value
