import json
from os import listdir

from database_controller import DatabaseController
from helper import *


class CardImporter:
    def __init__(self, data_folder_path):
        self.folder_path = data_folder_path + "Card/"
        self.table_name = "card"
        columns = ["id", "clan", "cost", "deck_limit", "fate", "glory", "honor", "influence_cost", "influence_pool",
                   "is_banned", "is_restricted", "is_unique", "military", "military_bonus", "name", "name_extra",
                   "political", "political_bonus", "role_restriction", "side", "strength", "strength_bonus",
                   "text", "type"]
        self.columns = create_comma_separated_string(columns)
        self.key = "id"
        self.update = create_update_on_conflict_statement(columns[1:])
        self.database_controller = DatabaseController()

    def execute_import(self):
        values = []
        for file in listdir(self.folder_path):
            with open(self.folder_path + file, encoding="UTF-8") as card_json_str:
                card_json = json.load(card_json_str)[0]
                value = self.get_value(card_json)
                values.append(value)
        values_string = ", ".join(values)
        self.database_controller.upsert(self.table_name, self.columns, values_string, self.key, self.update)

    def get_value(self, entry):
        value = "("
        value += "\'" + transform_string(entry["id"]) + "\', "
        value += get_nullable_value(entry, "clan") + ", "
        value += get_nullable_value(entry, "cost") + ", "
        value += get_nullable_value(entry, "deck_limit") + ", "
        value += get_nullable_value(entry, "fate") + ", "
        value += get_nullable_value(entry, "glory") + ", "
        value += get_nullable_value(entry, "honor") + ", "
        value += get_nullable_value(entry, "influence_cost") + ", "
        value += get_nullable_value(entry, "influence_pool") + ", "
        value += get_nullable_value(entry, "is_banned") + ", "
        value += get_nullable_value(entry, "is_restricted") + ", "
        value += get_nullable_value(entry, "unicity") + ", "
        value += get_nullable_value(entry, "military") + ", "
        value += get_nullable_value(entry, "military_bonus") + ", "
        value += get_nullable_value(entry, "name") + ", "
        value += get_nullable_value(entry, "name_extra") + ", "
        value += get_nullable_value(entry, "political") + ", "
        value += get_nullable_value(entry, "political_bonus") + ", "
        value += get_nullable_value(entry, "role_restriction") + ", "
        value += get_nullable_value(entry, "side") + ", "
        value += get_nullable_value(entry, "strength") + ", "
        value += get_nullable_value(entry, "strength_bonus") + ", "
        value += get_nullable_value(entry, "text") + ", "
        value += get_nullable_value(entry, "type")
        value += ")"
        return value
