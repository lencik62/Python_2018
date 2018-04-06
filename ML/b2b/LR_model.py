import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# %% read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

# %% traing the model
l_reg = linear_model.LinearRegression()
l_reg.fit(x_values,y_values)

# %% visualizing
plt.scatter(x_values,y_values)
plt.plot(x_values,l_reg.predict(x_values))
plt.show()