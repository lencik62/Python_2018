import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# %% read data
dataframe = pd.read_fwf('brain_body.txt')
# x_values = dataframe[['Brain']]
# y_values = dataframe[['Body']]

# # %% traing the model
# l_reg = linear_model.LinearRegression()
# l_reg.fit(x_values,y_values)

# # %% visualizing
# plt.scatter(x_values,y_values)
# plt.plot(x_values,l_reg.predict(x_values))
# plt.show()

dataframe = pd.DataFrame(dataframe,columns=['Brain','Body'])


x_values=dataframe['Brain'].values[:,np.newaxis]
y_values=dataframe['Body'].values[:,np.newaxis]

body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)
prediction=body_reg.predict(np.sort(x_values, axis=0))

plt.scatter(x_values, y_values)
plt.plot(np.sort(x_values, axis=0),prediction)
plt.show()