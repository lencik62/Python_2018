from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
def build_classifier():
    classifier = Sequential()
    classifier.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
    classifier.add(Dropout(0.2))
    classifier.add(LSTM(units = 50, return_sequences = True))
    classifier.add(Dropout(0.2))
    classifier.add(LSTM(units = 50, return_sequences = True))
    classifier.add(Dropout(0.2))
    classifier.add(LSTM(units = 50))
    classifier.add(Dropout(0.2))
    classifier.add(Dense(units = 1, activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'mean_squared_error')
    return classifier

def main():
    build_classifier()

if __name__ == '__main__':
    main()
