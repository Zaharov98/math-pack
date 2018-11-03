""" Poker hand classification """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import catboost as cb
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split

from data_reader import DataReader


pd.set_option('display.max_columns', 600)


def cv_and_test(X, y, Xte, yte):
    # 80/20 train test split cross-validation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    cat = cb.CatBoostClassifier(
        loss_function='MultiClassOneVsAll',
        random_seed=1234
    )
    cat_model = cat.fit(X_train, y_train, verbose=False)

    cat_predA = cat_model.predict(X_test, prediction_type='Class')
    cat_predLL = cat_model.predict(X_test, prediction_type='Probability')

    print("CV accuracy: {}".format(accuracy_score(y_test, cat_predA)))
    print("CV logloss: {}".format(log_loss(y_test, cat_predLL)))

    # Training with all X,y data, testing with Xte,yte
    cat_model = cat.fit(X, y, verbose=False)

    cat_predAt = cat_model.predict(Xte, prediction_type='Class')
    cat_predLLt = cat_model.predict(Xte, prediction_type='Probability')

    print("Test accuracy: {}".format(accuracy_score(yte, cat_predAt)))
    print("Test logloss: {}".format(log_loss(yte, cat_predLLt)))

    return cat_predA, cat_predLL, cat_predAt, cat_predLLt


def main():
    reader = DataReader('data/poker-hand-testing.data', 'data/poker-hand-training-true.data')
    testing = reader.get_test_data()
    training = reader.get_train_data()

    X = training.drop(['hand'], axis=1)
    y = training.hand
    Xte = testing.drop(['hand'], axis=1)
    yte = testing.hand

    print(testing.head())
    print(training.head())


if __name__ == '__main__':
    main()
