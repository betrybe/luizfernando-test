from inventory_report.inventory.inventory_interface import InventoryInterface
import csv


class ReadCSV(InventoryInterface):
    @classmethod
    def load_file(self, path_file):
        f = open(path_file, 'r')
        data = csv.DictReader(f)
        return list(data)
