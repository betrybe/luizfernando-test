import inventory_report.importer.importer as imp
from inventory_report.inventory.inventory_implement import ReadXML


class XmlImporter(imp.Importer):

    def import_data(self, path_file):
        try:
            if(path_file.endwith("xml")):
                return ReadXML.load_file(path_file)
        except ValueError as e:
            raise Exception('Arquivo inválido') from e
