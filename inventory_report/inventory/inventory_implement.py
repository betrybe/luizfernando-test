from inventory_report.inventory.inventory_interface import InventoryInterface
import csv
import json
import xmltodict


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


class ReadXML(InventoryInterface):
    @classmethod
    def load_file(self, path_file):
        self.__convertXML(path_file)

    def __convertXML(file):
        with open(file, "r") as f:
            data = xmltodict.parse(f.read())
            f.close()
        return json.dumps(data["dataset"]["record"])
