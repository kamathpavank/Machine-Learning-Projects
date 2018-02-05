# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:34:11 2018

@author: Pavan
"""

#importing liraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Encoding the categorical data
#Encoding theIndepedent variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
#Label encoder is use dto change he text to numbers
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
#To create dummy variables 
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X = X[:, 1:]

#spliting dataset into training and testing dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting  Multiple linear regression model for training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the test set results
y_pred = regressor.predict(X_test)

#Building the optional model usig backward elimination
import statsmodels.formula.api as sm
X = np.append(arr =np.ones((50,1)).astype(int), values =X , axis = 1)
#all possible predictors or featues
X_opt = X[:,[0,1,2,3,4,5]]
#fit full model with all possible predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

#remove feature 2 since it has highest P-value
X_opt = X[:,[0,1,3,4,5]]
#fit full model with one less predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

#remove feature 1 since it has highest P-value
X_opt = X[:,[0,3,4,5]]
#fit full model with two less predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

#remove feature 4 since it has highest P-value
X_opt = X[:,[0,3,5]]
#fit full model with three less predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

#remove feature 5 since it has highest P-value
X_opt = X[:,[0,3]]
#fit full model with four less predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

