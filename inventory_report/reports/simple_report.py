import pandas as pd
from datetime import date


class SimpleReport():

    @classmethod
    def generate(self, dictlist):

        df = pd.DataFrame.from_dict(dictlist)
        data_fabricacao_antiga = 'Data de fabricação mais antiga: {data}\n'\
            .format(data=df['data_de_fabricacao'].min())
        validade = df.loc[
            pd.to_datetime(
                df['data_de_validade']
                ) > pd.to_datetime(date.today())
            ]
        data_validade_proxima = 'Data de validade mais próxima: {data}\n'\
            .format(data=validade['data_de_validade'].min())
        formattext = data_fabricacao_antiga + data_validade_proxima
        return formattext
