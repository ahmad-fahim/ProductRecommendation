# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:57:09 2019

@author: fahim.ahmad
"""

from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import os



def get_dummy_feature(df, column_name):
    
    df[column_name] = df[column_name].astype('object')

    dummies=pd.get_dummies(df[column_name], prefix=column_name) 
    
    df=pd.concat([df,dummies],axis=1) 
    
    df.drop(column_name,axis=1,inplace=True)
    
    return df 


file_path = os.path.dirname(os.getcwd())+"\\Data_in_CSV\PROD_DATA.csv"
customer_df = pd.read_csv(file_path)

catcols = [ 'ACCOM_TYPE', 'CUSTOMER_CATEGORY','RISK_CATEGORY','SEX', 'MARITAL_STATUS', 'OCCUPN_CODE']



for col in catcols:
    customer_df = get_dummy_feature(customer_df , col )
    
features = customer_df.columns

customer_df = customer_df.dropna()


customer_df = pd.DataFrame(customer_df,columns=features)

customer_df.loc[(customer_df.PRODUCTCATEGORY == 'Saving'),'PRODUCTCATEGORY']='1'
customer_df.loc[(customer_df.PRODUCTCATEGORY == 'Current'),'PRODUCTCATEGORY']='2'
customer_df.loc[(customer_df.PRODUCTCATEGORY == 'Fixed'),'PRODUCTCATEGORY']='3'
customer_df.loc[(customer_df.PRODUCTCATEGORY == 'DPS'),'PRODUCTCATEGORY']='4'
customer_df.loc[(customer_df.PRODUCTCATEGORY == 'Conti'),'PRODUCTCATEGORY']='5'
customer_df.loc[(customer_df.PRODUCTCATEGORY == 'Term'),'PRODUCTCATEGORY']='6'

customer_df['PRODUCTCATEGORY'] = pd.to_numeric(customer_df['PRODUCTCATEGORY'])

y = customer_df['PRODUCTCATEGORY']

X = customer_df.copy()

del X['CUSTOMER_CODE']
del X['PRODUCTCATEGORY']
del X['CUSTOMER_TYPE']
del X['CUSTOMER_SEGMENT_CODE']
del X['ACNUM']

del X['OPENING_DURATION']	
del X['ACCOUNT_OPEN_WAY']	
del X['INOP_ACNT']	
del X['MODE_OF_OPERN']	
del X['DORMANT_ACNT']	
del X['DB_FREEZED']	
del X['CR_FREEZED']
del X['ACCOUNT_CLOSE_FLAGE']	
del X['TRANSFRD_BRNCODE']	
del X['ONLINE_TRAN_ALLOWED']

feature_name = list(X.columns)
num_feats=30






X_norm = MinMaxScaler().fit_transform(X)

embeded_lr_selector = SelectFromModel(LogisticRegression(penalty="l1"), max_features=num_feats)
embeded_lr_selector.fit(X_norm, y)

embeded_lr_support = embeded_lr_selector.get_support()
embeded_lr_feature = X.loc[:,embeded_lr_support].columns.tolist()
print(str(len(embeded_lr_feature)), 'selected features')

for ordered_features in sorted(embeded_lr_feature): 
    print(ordered_features) 