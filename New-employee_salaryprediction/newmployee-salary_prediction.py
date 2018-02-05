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
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


#spliting dataset into training and testing dataset
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
#Transform origial matrix in polynomial form
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
#fit transformed matrix
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Visualizing the Linear regression reesults
plt.scatter(X, y, color= 'red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truth  or bluf(Linear Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()
#Visualizing the Polynomial regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color= 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth  or bluf(Polynomial Regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#Predicting a new result with Linear Regression
lin_reg.predict(6.5)

#Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))
