# Import the libraries
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier

# Load the dataset
dataset = pd.read_csv('yellDataV1.csv')

# Split dependent variable (y) and independent variable (X)

# y = dataset.iloc[:, 1]
# X = dataset.iloc[:, 0]
dataset['split'] = np.random.randn(dataset.shape[0], 1)
yellSep = np.random.rand(len(dataset)) <= 0.7

train = dataset[yellSep]
test = dataset[~yellSep]

y_train = train.iloc[:, 1]
X_train = train.iloc[:, 0]

X_test = test.iloc[:, 0]
y_test = test.iloc[:, 1]

# Define target names to teach the machine the proper labels
targetNames = ['K1', 'K2', 'K3', 'K4']

# Model the classifier
classifier = Pipeline([
                       ('vectorizer', CountVectorizer()),
                       ('tfidf', TfidfTransformer()),
                       ('clf', OneVsRestClassifier(LinearSVC()))])

classifier.fit(X_train, y_train)

predicted = classifier.predict(X_test)