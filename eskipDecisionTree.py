# Importing the required packages 
#import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.cross_validation import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
  
# Load the dataset
dataset = pd.read_csv('yellDataV2.csv')

# Print the dataset lenght, shape and observations
print ("Dataset Lenght: ", len(dataset))
print ("Dataset Shape: ", dataset.shape)
print ("Dataset: ", dataset.head())
                            
# Pre-processing
# dataset['Terms'].head()
    # Transforming to lower case
dataset['Terms'] = dataset['Terms'].apply(lambda x: " ".join(x.lower() for x in x.split()))

    # Removing Punctuation
dataset['Terms'] = dataset['Terms'].str.replace('[^\w\s]','')

    # Removing StopWords
from nltk.corpus import stopwords
# nltk.download('stopwords')
stop = stopwords.words('english')
dataset['Terms'] = dataset['Terms'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

    # Checking common words
freq = pd.Series(' '.join(dataset['Terms']).split()).value_counts()
# print(freq)    
    
    # Spelling correction
from textblob import TextBlob
dataset['Terms'].apply(lambda x: str(TextBlob(x).correct()))

    # Tokenization
#TextBlob(dataset['Terms']).words

    # Lemmatization
from textblob import Word   
dataset['Terms'] = dataset['Terms'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))  
 
    # Label encoder
from sklearn import preprocessing

le = preprocessing.LabelEncoder()
dataset['Terms_factor'] = le.fit_transform(dataset.Terms)
dataset['Term_Criterion_Label_factor'] = le.fit_transform(dataset.Term_Criterion_Label)

# Split the dataset to dependent variable (y) and independent variable (X)
def splitdataset(dataset):
    
    X = dataset[['Terms_factor']]
    Y = dataset[['Term_Criterion_Label_factor']]

    # Spliting the dataset into train (70%) and test (30%)
    X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                        test_size = 0.3,
                                                        random_state = 100)
    return X,Y, X_train, X_test, y_train, y_test


# Train the model using Gini Index
def giniIndexTrain(X_train, X_test, y_train):
    # Create the classifier object
    clfGini = DecisionTreeClassifier(criterion = "gini",
                                     random_state = 100,
                                     max_depth = 3, min_samples_leaf = 5)
    # Perform the train
    clfGini.fit(X_train, y_train)

    return clfGini    
    
    
# Make prediction
def prediction(X_test, clfGini):
    # Predict on test using Gini Index
    y_pred = clfGini.predict(X_test)
    print ("Predicted values:")
    print (y_pred)
    return y_pred
    

# Calculate accuracy
def calcAccuracy(y_test, y_pred):
    print ("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
    print ("Accuracy: ", accuracy_score(y_test, y_pred)*100)
    print ("Report: ", classification_report(y_test, y_pred))
      

# Driver code 
def main():
    # Building phase
    data = dataset
    X,Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clfGini = giniIndexTrain(X_train, X_test, y_train)
    
    # Operational phase
    print ("Results using Gini Index:")
    # Prediction using Gini
    y_pred_Gini = prediction(X_test, clfGini)
    calcAccuracy(y_test, y_pred_Gini)

# Call main function
if __name__=="__main__":
    main()
      
        