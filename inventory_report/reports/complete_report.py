from inventory_report.reports.simple_report import SimpleReport
import pandas as pd


class CompleteReport():

    @classmethod
    def generate(self, dictlist):
        df = pd.DataFrame.from_dict(dictlist)
        simple = SimpleReport.generate(dictlist)
        format_products = ""
        for id, name in enumerate(
                df['nome_da_empresa'].value_counts(sort=True).index.tolist()
        ):
            format_products += "- {name}: {count}\n"\
                .format(
                    name=name, count=df['nome_da_empresa']
                    .value_counts()[id]
                )

        complete = "Produtos estocados por empresa: \n" \
                   + "{data}".format(data=format_products)
        return simple + "\n" + complete
