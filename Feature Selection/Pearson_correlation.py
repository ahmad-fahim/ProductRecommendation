# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:53:56 2019

@author: fahim.ahmad
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import seaborn as sns

import matplotlib.pyplot as plt
sns.set(style="ticks")

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
flatui = sns.color_palette(flatui)

# https://towardsdatascience.com/the-search-for-categorical-correlation-a1cf7f1888c9
import seaborn as sns


def cor_selector(X, y,num_feats):
    cor_list = []
    feature_name = X.columns.tolist()
    # calculate the correlation with y for each feature
    for i in X.columns.tolist():
        #print(i)
        cor = np.corrcoef(X[i], y)[0,1]
        #print(cor)
        cor_list.append(cor)
    # replace NaN with 0
    cor_list = [0 if np.isnan(i) else i for i in cor_list]
    # feature name
    cor_feature = X.iloc[:,np.argsort(np.abs(cor_list))[-num_feats:]].columns.tolist()
    # feature selection? 0 for not select, 1 for select
    cor_support = [True if i in cor_feature else False for i in feature_name]
    return cor_support, cor_feature

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

customer_df.loc[customer_df.PRODUCTCATEGORY <= 4, 'IsADeposit'] = True
customer_df.loc[customer_df.PRODUCTCATEGORY > 4, 'IsADeposit'] = False

y = customer_df['IsADeposit']

X = customer_df.copy()

del X['CUSTOMER_CODE']
del X['PRODUCTCATEGORY']
del X['CUSTOMER_TYPE']
del X['CUSTOMER_SEGMENT_CODE']
del X['ACNUM']
del X['IsADeposit']

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



cor_support, cor_feature = cor_selector(X, y,num_feats)

print(str(len(cor_feature)), 'selected features')


for ordered_features in sorted(cor_feature): 
    print(ordered_features) 

