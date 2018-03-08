# %% project imports using tensorflow backend
import time
import warnings
import numpy as np
from numpy import newaxis
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import matplotlib.pyplot as plt

# %%
X_train, Y_train, X_test, Y_test = LSTM.load_data("", 50, True)
