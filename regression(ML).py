# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:53:53 2018

@author: abhishek chandel
"""

import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation,svm
from sklearn.linear_model import LinearRegression 


quandl.ApiConfig.api_key = 'dh9UG1TdMM3REhynyMLS'
df = quandl.get_table('WIKI/PRICES', date='1999-11-18', ticker='A')
 
print(df)
quandl_df = df
quandl_df= [["adj_open","adj _high","adj_low","adj_close","adj_volume"]]
 
df['PCT-Change'] =(df['adj_close']-df['adj_open'])/df['adj_open']*100.0
df['HL_PCT'] = (df['adj_high']-df['adj_close'])/df['adj_close']*100.0
 
df1 = df[['adj_close','adj_volume','HL_PCT','PCT-Change']]
 
forecast_col = 'adj_close'
df.fillna(-99999,inplace= True)
forecast_out = int(math.ceil(0.1*len(df)))

df1['label'] = df[forecast_col].shift(-forecast_out)