import json
from abc import ABC, abstractmethod


class Importer(ABC):
    def execute_import(self):
        with open(self.data_file, encoding="UTF-8") as jsons_str:
            jsons = json.load(jsons_str)
            values = []
            for cycle in jsons:
                value = self.get_value(cycle)
                values.append(value)
            values_string = ", ".join(values)
            self.database_controller.upsert(self.table_name, self.columns, values_string, self.key, self.update)

    @abstractmethod
    def get_value(self, entry):
        pass
