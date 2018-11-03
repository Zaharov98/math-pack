""" Data reader class """

import pandas as pd


class DataReader:
    def __init__(self, train_data_path):
        self.train_data = train_data_path

    def get_train_data(self):
        return pd.read_csv(self.train_data)
