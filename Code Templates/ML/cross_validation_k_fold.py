
# Classifier imports as example

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier

# Cross validate
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_predict

classifier_ = KerasClassifier(build_fn = build_classifier, batch_size = 10, nb_epoch = 100)
scores = cross_val_predict(estimator = classifier_, X = "X Data put here", y = "Y data put here", cv = 10, n_jobs = -1)