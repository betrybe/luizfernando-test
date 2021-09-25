from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import inventory_report.inventory.inventory_implement as methodfile


class Inventory():

    @classmethod
    def import_data(self, path_file, type_report):
        file = ''
        if path_file.endswith("csv"):
            file = methodfile.ReadCSV.load_file(path_file)
        elif path_file.endswith("json"):
            file = methodfile.ReadJSON.load_file(path_file)
        elif path_file.endswith("xml"):
            file = methodfile.ReadXML.load_file(path_file)
        else:
            print("Extensão não encontrada")

        return self.__report(file, type_report)

    def __report(file, type):
        if type == "simples":
            return SimpleReport.generate(file)
        elif type == "completo":
            return CompleteReport.generate(file)
        else:
            print("Tipo não encontrado")
