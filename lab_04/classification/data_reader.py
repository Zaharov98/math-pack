""" Test and train data reader """

import pandas as pd


class DataReader:
    def __init__(self, test_data_path, train_data_path):
        self.test_data = test_data_path
        self.train_data = train_data_path

    def get_train_data(self):
        return pd.read_csv(self.train_data,
                           names=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand', ])

    def get_test_data(self):
        return pd.read_csv(self.test_data,
                           names=['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'hand', ])
