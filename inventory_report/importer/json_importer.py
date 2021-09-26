import inventory_report.importer.importer as imp
from inventory_report.inventory.inventory_implement import ReadJSON


class JsonImporter(imp.Importer):

    def import_data(self, path_file):
        try:
            if(path_file.endwith("json")):
                return ReadJSON.load_file(path_file)
        except ValueError as e:
            raise Exception('Arquivo inválido') from e
