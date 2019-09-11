# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:38:47 2019

@author: PAT
"""

import warnings
warnings.filterwarnings("ignore")

import os
import sys


import pandas as pd
import seaborn  as sb
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize']=9,8
plt.style.use('seaborn-whitegrid')

import warnings
warnings.filterwarnings("ignore")

import numpy as np
from scipy import stats
import sklearn
import geopy
from geopy.distance import geodesic

#-----------plotting
import plotly.graph_objs as go
import plotly.offline as py
from pandas.plotting import scatter_matrix


#-------------------For Algorithms
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVC

#---------scoring
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import roc_curve,roc_auc_score
#-----Utilities
#from scipy.stats import kurtosis,skew
from scipy.stats import chi2_contingency


from sklearn.model_selection import KFold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from sklearn.preprocessing import LabelEncoder

from imblearn.combine import SMOTETomek#combine undersampling and oversampling
