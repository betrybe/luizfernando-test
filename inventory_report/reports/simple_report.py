import pandas as pd


class SimpleReport():

    @classmethod
    def generate(self, dictlist):

        df = pd.DataFrame.from_dict(dictlist)
        data_fabricacao_antiga = 'Data de fabricação mais antiga: {data}\n'\
            .format(data=df['data_de_fabricacao'].min())
        formattext = data_fabricacao_antiga
        return formattext
