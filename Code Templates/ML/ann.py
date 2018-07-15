from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
def build_classifier(data):
    classifier = Sequential()
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = data.shape[1]))
    # dropout is to reduce the chances of overfitting {p = .1-.4}
    classifier.add(Dropout(rate = .1))
    classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dropout(rate = .1))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier


__doc__ = "THIS CLASSIFIER WAS USED TO FIND CORRELATION BETWEEN PROPERTY AND IT'S PRICE"

def main():
    build_classifier([])

if __name__ == '__main__':
    main()
