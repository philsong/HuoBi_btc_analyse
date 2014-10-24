"""
do some backtest
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt

def gen_dataset_from_price(df,step=100):
    """
    df['price'] is required
    """
    price_list = df['price']
    X = [price_list.values[i:i+step] for i in range(int(len(price_list)/10))]
    Y = [price_list.values[i+step] for i in range(int(len(price_list)/10))]
    return X,Y

def do_train(hdf='/home/yacc/packages/btc-trade-result-history/btc_all.h5',    dataset = 'trade_2014_10_11_with_id'):
    """
    TODO add some comments
    """
    params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 1,'learning_rate': 0.01, 'loss': 'ls'}
    clf = GradientBoostingRegressor(verbose=True,**params)

    h = pd.HDFStore(hdf,'r')

    X,y = gen_dataset_from_price(h[dataset],step=200)

    print('data generated.')
    offset = int(len(X) * 0.1)
    X_train, y_train = X[:offset], y[:offset]
    X_test, y_test = X[offset:], y[offset:]

    clf.fit(X_train,y_train)

    plt.plot(y_test,'r-')
    plt.plot(clf.predict(X_test),'b-')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        do_train()  
    else:
        do_train(hdf=sys.argv[1])
