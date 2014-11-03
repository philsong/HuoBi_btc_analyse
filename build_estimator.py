# -*- encoding=utf8 -*-

import pandas as pd
import numpy as np
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.neural_network import BernoulliRBM
from sklearn.ensemble import GradientBoostingRegressor

class Predicator(object):
    def initialize(self):
        """
        setup classifier normally a pipeline
        """
        clf_1 = BernoulliRBM(n_components=1024,learning_rate=0.01,n_iter=100)
        clf_2 = BernoulliRBM(n_components=512,learning_rate=0.01,n_iter=100)
        clf_3 = BernoulliRBM(n_components=256,learning_rate=0.01,n_iter=200)
        clf_last = GradientBoostingRegressor()
        clf = Pipeline(steps=[('clf_1',clf_1),('clf_2',clf_2),('clf_3',clf_3),('clf_last',clf_last)])
        params = {}
        data_format = {}

    def handle_data(self):
        """
        """
