import inventory_report.importer.importer as imp
from inventory_report.inventory.inventory_implement import ReadCSV


class CsvImporter(imp.Importer):

    def import_data(self, path_file):
        try:
            ReadCSV.load_file(path_file)
        except ValueError:
            print("Arquivo inválido")
