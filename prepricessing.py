import pandas as pd
import jdatetime as jt


data_row = pd.read_csv('data/train_Data.csv')
print(data_row)


class Preprocessing(object):
    def __init__(self, data, time_data_column):
        self.data = data
        self.time_data = time_data_column

    def setup_index(self):
        pd.set_index('InvoiceDate', self.data)




