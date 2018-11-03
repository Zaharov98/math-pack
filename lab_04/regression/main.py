""" Linear regression prediction """

import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

from data_reader import DataReader


def display_linear_regression(prediction_rfr, train_y):
    plt.figure(figsize=(5, 5))
    plt.scatter(prediction_rfr, train_y)

    plt.plot([0, 1000], [0, 1000], color='red')
    plt.xlim(-100, 1000)
    plt.ylim(-100, 1000)

    plt.xlabel('prediction')
    plt.ylabel('train_y')
    plt.title('Random Forest Regression Model')

    plt.show()


def get_prediction_rfr(train_x, train_y):
    rfr = RandomForestRegressor().fit(train_x, train_y)
    return rfr.predict(train_x)


def main():
    reader = DataReader('./data/hour.csv')
    train_data = reader.get_train_data()

    train_x = train_data.drop(['dteday', 'cnt', 'casual', 'registered'], axis=1)
    train_y = train_data['cnt'].values

    prediction_rfr = get_prediction_rfr(train_x, train_y)
    display_linear_regression(prediction_rfr, train_y)


if __name__ == '__main__':
    main()
