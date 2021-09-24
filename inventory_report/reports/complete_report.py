from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:

    @classmethod
    def generate(self, dictlist):
        simple = SimpleReport.generate(dictlist)
        return simple
