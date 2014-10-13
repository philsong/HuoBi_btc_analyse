"""
do some backtest
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

def gen_dataset_from_price(df,step=100):
    """
    df['price'] is required
    """
    price_list = df['price']
    X = [price_list.values[i:i+step] for i in range(len(price_list))]
    Y = price_list.values[step:]
    return X,Y


def do_train(hdf='/home/yacc/packages/btc-trade-result-history/btc_all.h5',    dataset = 'trade_2014_10_11_with_id'):
    """
    TODO add some comments
    """
    params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,'learning_rate': 0.01, 'loss': 'ls'}
    clf = GradientBoostingRegressor()

    h = pd.HDFStore(hdf,'r')

    X,y = gen_dataset_from_price(h[dataset],step=200)
    offset = int(len(X) * 0.1)
    X_train, y_train = X[:offset], y[:offset]
    X_test, y_test = X[offset:], y[offset:]

    clf.fit(X_train,y_train)

    import matplotlib.pyplot as plt
    plt.plot(y_test,'r-')
    plt.plot(clf.predict(X_test),'b-')

if __name__ == '__main__':
    do_train()
