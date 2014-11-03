"""
do some backtest
"""
from __future__ import print_function
import sys
import pandas as pd
import numpy as np
import pickle
from numba import jit
import sklearn
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.neural_network import BernoulliRBM
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import Pipeline

def gen_dataset_from_price(df,step=200,ahead=10,percent=0.1):
    """
    df['price'] is required
    """
    if percent>1.0 or percent<0.0:
        raise Exception('Error percentage!')
    price_list = df['price']
    X = []
    Y = []
    for i in range( int(len(price_list)*percent) ):
        print('\r generating data number: {0}\r'.format(i),file=sys.stdout,end=" ")
        X.append(price_list.values[i:i+step])
        Y.append(np.average(price_list.values[i+step:i+step+ahead]))
    #X = [price_list.values[i:i+step] for i in range(int(len(price_list)/2))]
    #Y = [np.average(price_list.values[i+step] for i in range(int(len(price_list)/2))]
    return X,Y

def do_train(hdf='/home/yacc/packages/btc-trade-result-history/btc_all_in_one.h5',    dataset = 'a'):
    """
    TODO add some comments
    """
    h = pd.HDFStore(hdf,'r')
    df = h[dataset]
    h.close()
    X,y = gen_dataset_from_price(df,step=200,ahead=20,percent=0.01)
    print('\n data generated.')
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33)
    print('train test split done.')
    #params = {'learning_rate': 0.1,'n_iter':20}
    #reg_clf = GradientBoostingRegressor(verbose=True,**params)
    reg_clf = SGDRegressor(verbose=True,n_iter=100)
    clf_rbm1 = BernoulliRBM(n_components=1024,verbose=True)
    clf_rbm2 = BernoulliRBM(n_components=512,verbose=True)
    clf_rbm3 = BernoulliRBM(n_components=256,verbose=True)
    clf = Pipeline(steps=[('clf1',clf_rbm1),('clf2',clf_rbm2),('clf3',clf_rbm3),('clf_last',reg_clf)])
    print('start training')
    clf.fit(X_train,y_train)
    import datetime
    with open('clf_pipeline_pick.pkl','a+') as f:
        pickle.dump(clf,f)
        print('pickle done.')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        do_train()
    else:
        do_train(hdf=sys.argv[1])
