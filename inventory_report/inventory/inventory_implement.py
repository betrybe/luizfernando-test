from inventory_report.inventory.inventory_interface import InventoryInterface
import csv
import json


class ReadCSV(InventoryInterface):
    @classmethod
    def load_file(self, path_file):
        f = open(path_file, 'r')
        data = csv.DictReader(f)
        return list(data)


class ReadJSON(InventoryInterface):
    @classmethod
    def load_file(self, path_file):
        f = open(path_file, 'r')
        data = json.load(f)
        return data
