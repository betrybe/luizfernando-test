import inventory_report.importer.importer as imp


class XmlImporter(imp.Importer):

    def import_data(self, path_file):
        try:
            pass
        except ValueError:
            print("Arquivo inválido")
