import json
from os import listdir

from importer.card_importer import CardImporter
from importer.cycle_importer import CycleImporter
from importer.label_importer import LabelImporter
from importer.packs_importer import PackImporter

path = "./fiveringsdb-data/json/"

print("Importing Cycles...")
CycleImporter(path).execute_import()
print("Importing Packs...")
PackImporter(path).execute_import()
print("Importing Labels:...")
LabelImporter(path).execute_import()
print("importing Cards...")
CardImporter(path).execute_import()

# for file in listdir(path):
#     with open(path + file, encoding="UTF-8") as card_json:
#         card = json.load(card_json)[0]
#         print("### LOG: importing " + card["name"])
#         database_controller.execute_query("""
#
#         """)
