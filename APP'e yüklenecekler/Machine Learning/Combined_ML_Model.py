#!/usr/bin/env python
# coding: utf-8

# In[18]:



import pandas as pd
from pandas import DataFrame as df
from sklearn import svm
from sklearn.metrics import mean_squared_error
import math
import numpy as np
from sklearn.model_selection import train_test_split


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor as rf




trainges = pd.read_excel(r'C:\Users\Msi\Desktop\GES_ML.xlsx')
trainges = df(trainges)
df.head(trainges)

trainges = trainges.iloc[:, 1:6]
df.head(trainges)


ges_x = trainges.iloc[:, 0:3]
df.head(ges_x)

ges_x.columns = ['Irradiance', 'Temperature','Tilt']

ges_y = trainges.iloc[:, 4]
ges_y = df(ges_y)
df.head(ges_y)

X_traing, X_valg, y_traing, y_valg = train_test_split(ges_x, ges_y, test_size=0.3)
print(X_traing.shape, y_traing.shape)
print(X_valg.shape, y_valg.shape)


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

rfges = RandomForestRegressor(
    n_estimators=600,  # Number of trees in the forest
    max_depth=8,  # Maximum depth of the tree
    min_samples_split=5,  # Minimum number of samples required to split a node
    min_samples_leaf=1,  # Minimum number of samples required at a leaf node
    random_state=42,
)



rfges.fit(ges_x, ges_y)



restrain = pd.read_excel('RESML.xlsx')
restrain = df(restrain)
df.head(restrain)

restrain = restrain.iloc[:, 1:7]
df.head(restrain)

import seaborn as sns
import math


restrain['s2'] = restrain['Speed'] ** 2
restrain['p6'] = restrain['Pressure'] ** 6


df.head(restrain)

res_x = restrain.iloc[:, [6,7]]
df.head(res_x)

res_x.columns = [ 's2','p6']

res_y = restrain.iloc[:, 5]
res_y = df(res_y)
df.head(res_y)

X_trainr, X_valr, y_trainr, y_valr = train_test_split(res_x, res_y, test_size=0.3)
print(X_trainr.shape, y_trainr.shape)
print(X_valr.shape, y_valr.shape)



rfres = RandomForestRegressor(
    n_estimators=200,  # Number of trees in the forest
    max_depth=None,  # Maximum depth of the tree
    min_samples_split=2,  # Minimum number of samples required to split a node
    min_samples_leaf=1,  # Minimum number of samples required at a leaf node
    random_state=42,
)
rfres.fit(res_x, res_y)




# load the input Excel file
input_data = pd.read_excel('state_defnew.xlsx')
tilt = float(input('Please enter the tilt value for your project: '))

input_data['Tilt'] = tilt
input_data['s2min'] = input_data['Speedmin'] ** 2
input_data['p6max'] = input_data['Pressuremax'] ** 6

input_data['s2max'] = input_data['Speedmax'] ** 2
input_data['p6min'] = input_data['Pressuremin'] ** 6

input_data['GESminPower'] = np.nan
input_data['GESmaxPower'] = np.nan

input_data['RESminPower'] = np.nan
input_data['RESmaxPower'] = np.nan

# extract the feature values for both predictions
x_input1 = input_data[['Irradiancemin', 'Temperaturemin', 'Tilt']]
x_input2 = input_data[['Irradiancemax','Temperaturemax', 'Tilt']]

x_input3 = input_data[['s2min', 'p6max']]
x_input4 = input_data[['s2max','p6min']]

# use the trained model to predict the power output for both inputs
y_pred1 = rfges.predict(x_input1)
y_pred2 = rfges.predict(x_input2)

y_pred3 = rfres.predict(x_input3)
y_pred4 = rfres.predict(x_input4)


# add the predicted power values as new columns to the input DataFrame
input_data['GESminPower'] = y_pred1
input_data['GESmaxPower'] = y_pred2
input_data['RESminPower'] = y_pred3
input_data['RESmaxPower'] = y_pred4

# save the updated DataFrame to the input Excel file
input_data.to_excel('CombinedPrediction.xlsx', index=False)




