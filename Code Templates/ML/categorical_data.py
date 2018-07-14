# Data Preprocessing
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Importing the dataset
data_path = input("Where is the data located?")
dataset = pd.read_csv(data_path)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

## Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X)
X = imputer.transform(X)

## Encoding categorical data

### Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

### Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)