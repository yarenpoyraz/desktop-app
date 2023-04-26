#!/usr/bin/env python
# coding: utf-8

# In[11]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
from pandas import DataFrame as df
from sklearn import svm
from sklearn.metrics import mean_squared_error
import math
import numpy as np
from sklearn.model_selection import train_test_split


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor as rf


# In[2]:

train = pd.read_excel(r'C:\Users\Msi\Desktop\GES_ML.xlsx')
train = df(train)
df.head(train)

# In[3]:
train = train.iloc[:, 1:6]
df.head(train)


train_x = train.iloc[:, 0:3]
df.head(train_x)


# In[4]:


train_x.columns = ['Irradiance', 'Temperature','Tilt']

train_y = train.iloc[:, 4]
train_y = df(train_y)
df.head(train_y)


# In[5]:


X_train, X_val, y_train, y_val = train_test_split(train_x, train_y, test_size=0.3)
print(X_train.shape, y_train.shape)
print(X_val.shape, y_val.shape)


# In[6]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

rf = RandomForestRegressor(
    n_estimators=600,  # Number of trees in the forest
    max_depth=8,  # Maximum depth of the tree
    min_samples_split=5,  # Minimum number of samples required to split a node
    min_samples_leaf=1,  # Minimum number of samples required at a leaf node
    random_state=42,
)


# In[7]:


rf.fit(train_x, train_y)

y_pred = rf.predict(X_val)
y_val_array = np.array(y_val)
y_val_array

np.sqrt(mean_squared_error(y_pred,y_val_array))


# In[8]:


import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error


y_pred = rf.predict(train_x)
mse= mean_squared_error(train_y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(train_y, y_pred)
mape= mean_absolute_percentage_error(train_y,y_pred)
mae = mean_absolute_error(train_y,y_pred)

print('Mean Squared Error: {:.2f}'.format(mse))
print('R^2 score: {:.2f}'.format(r2))
print('Root mse: {:.2f}'.format(rmse))
print("MAE:", mae)
print("MAPE:", mape)


# In[13]:


# load the input Excel file
input_data = pd.read_excel('state_defnew.xlsx')
tilt = float(input('Please enter the tilt value for your project: '))

# add new columns with the tilt value
input_data['Tilt'] = tilt
input_data['GESminPower'] = np.nan
input_data['GESmaxPower'] = np.nan

# extract the feature values for both predictions
x_input1 = input_data[['Irradiancemin', 'Temperaturemin', 'Tilt']]
x_input2 = input_data[['Irradiancemax','Temperaturemax', 'Tilt']]

# use the trained model to predict the power output for both inputs
y_pred1 = rf.predict(x_input1)
y_pred2 = rf.predict(x_input2)

# add the predicted power values as new columns to the input DataFrame
input_data['GESminPower'] = y_pred1
input_data['GESmaxPower'] = y_pred2

# save the updated DataFrame to the input Excel file
input_data.to_excel('GESPrediction.xlsx', index=False)






# In[9]:


import numpy as np

input_features = [72, -7.6, 25]

# reshape the input features into a 2D array 232,8676
input_features = np.array(input_features).reshape(1, -1)

# make the prediction
predicted_y = rf.predict(input_features)

# print the predicted power
print("Predicted power:", predicted_y[0]) 


# In[ ]:




