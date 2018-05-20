# Natural Language Processing

# Importing the libraries
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sn

# Importing the dataset
# make the delimter form , to tab and then ignore quotes
dataset = pd.read_csv('training_set_rel3.tsv',
                      delimiter='\t',
                      quoting=3,
                      encoding="ISO-8859-1")


# Cleaning the texts
import re
# import nltk
# nltk.download('stopwords')  # download a list of
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, len(dataset)):
    # for each elem in dataset remove all elem that are not
    review = re.sub('[^a-zA-Z]', ' ', dataset['essay'][i])
    review = review.lower()
    review = review.split()
    # converts the compound word into root word
    ps = PorterStemmer()
    # for all the words in the review only return word that are not in stopwords(english package)
    review = [ps.stem(word)
              for word in review
              if not word in set(stopwords.words('english'))]
    if(i%1000==0):
        print(i,"Done" ,i/len(dataset))
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
# have a mox limit of 1500
cv = CountVectorizer(max_features=2000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values
print("fitted and ready")

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

import cPickle
# save the classifier
from sklearn.externals import joblib
_ = joblib.dump(clf, "billy1.joblib.pkl",compress=9)
#clf2 = joblib.load(filename)
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
TP = cm[1][1]
TN = cm[0][0]
FN = cm[1][0]
FP = cm[0][1]
Accuracy = (TP+TN)/np.sum(cm)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1Score = (2 * Precision * Recall) / (Precision + Recall)
print(F1Score)






dataset = pd.read_csv('test_set.tsv',
                      delimiter='\t',
                      quoting=3,
                      encoding="ISO-8859-1")

# Cleaning the texts

corpus = []
for i in range(0, len(dataset)):
    # for each elem in dataset remove all elem that are not
    review = re.sub('[^a-zA-Z]', ' ', dataset['essay'][i])
    review = review.lower()
    review = review.split()
    # converts the compound word into root word
    ps = PorterStemmer()
    # for all the words in the review only return word that are not in stopwords(english package)
    review = [ps.stem(word)
              for word in review
              if not word in set(stopwords.words('english'))]
    if(i%1000==0):
        print(i,"Done" ,i/len(dataset))
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
# have a mox limit of 1500
cv = CountVectorizer(max_features=2000)
X_testo = cv.fit_transform(corpus).toarray()
y_testo = dataset.iloc[:,1].values
print("fitted and ready")

# Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X, y)

# save the classifier
_ = joblib.dump(clf, "billy2.joblib.pkl",compress=9)
#clf2 = joblib.load(filename)
# Predicting the Test set results
y_pred = classifier.predict(X_testo)

# Making the Confusion Matrix
cm = confusion_matrix(y_testo, y_pred)
TP = cm[1][1]
TN = cm[0][0]
FN = cm[1][0]
FP = cm[0][1]
Accuracy = (TP+TN)/np.sum(cm)
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)
F1Score = (2 * Precision * Recall) / (Precision + Recall)
print(F1Score)