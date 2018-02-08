
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
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y= y.reshape(-1, 1)
y = sc_y.fit_transform(y)


#Fitting  Regression Model to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

#Predicting a new result with Polynomial Regression
y_pred = regressor.predict(sc_transform(6.5)

#Visualizing the  Regression results
plt.scatter(X, y, color= 'red')
plt.plot(X,regressor.predict(X), color='blue')
plt.title('Truth  or bluf(Regression model)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()np.array 

#Visualizing the  SVR results
plt.scatter(X, y, color= 'red')
plt.plot(X,regressor.predict(X), color='blue')
plt.title('Truth  or bluf(SVR)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()
 