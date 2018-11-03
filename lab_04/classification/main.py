""" Poker hand classification """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import catboost as cb
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split

from data_reader import DataReader


pd.set_option('display.max_columns', 600)


def display_logarithmic_histogram(yte, cat_predAt):
    # Logarithmic Histogram
    plt.hist((np.reshape(cat_predAt, (yte.shape[0],)), yte), bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], log=True)
    plt.legend(labels=('preds', 'test'))
    plt.show()


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


def combine_data(all_data):
    def bincount_2d_vectorized(a):
        N = a.max() + 1
        a_offs = a + np.arange(a.shape[0])[:, None] * N
        return np.bincount(a_offs.ravel(), minlength=a.shape[0] * N).reshape(-1, N)

    S = all_data.iloc[:, [0, 2, 4, 6, 8]].astype(int)
    S = pd.DataFrame(bincount_2d_vectorized(S.values), columns=['suit0', 'suit1', 'suit2', 'suit3', 'suit4'])
    all_data = pd.merge(all_data, S, how='left', left_index=True, right_index=True).drop(['suit0'], axis=1)

    R = all_data.iloc[:, np.arange(1, 10, 2)].astype(int)
    cols = ['rank{}'.format(x) for x in range(0, 14, 1)]
    R = pd.DataFrame(bincount_2d_vectorized(R.values), columns=cols)
    all_data = pd.merge(all_data, R, how='left', left_index=True, right_index=True).drop(['rank0'], axis=1)

    X = all_data.iloc[:25010, :].drop(['hand'], axis=1)
    Xte = all_data.iloc[25010:, :].drop(['hand'], axis=1)

    return X, Xte


def main():
    reader = DataReader('data/poker-hand-testing.data', 'data/poker-hand-training-true.data')
    testing = reader.get_test_data()
    training = reader.get_train_data()

    y = training.hand
    yte = testing.hand

    # X = training.drop(['hand'],axis=1)
    # Xte = testing.drop(['hand'],axis=1)
    X, Xte = combine_data(pd.concat([training, testing, ]).reset_index(drop=True))

    cat_predA, cat_predLL, cat_predAt, cat_predLLt = cv_and_test(X, y, Xte, yte)
    display_logarithmic_histogram(yte, cat_predAt)


if __name__ == '__main__':
    main()
