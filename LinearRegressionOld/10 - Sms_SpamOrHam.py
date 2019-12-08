# Predict if message is spam or ham
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# Read the CSV file and create a data frame.
my_data_frame = pd.read_csv('D:\\myPython\\my_numpy\\Course-DataSciene\\SourceDataFor_Sms_SpamOrHam.csv', encoding='latin-1')

# # Lets read top 5 records to view our data frame
# print(my_data_frame.head())
#
# # Lets read bottom 5 records to view our data frame
# print(my_data_frame.tail())
# Lets check how many message in data base are spam and ham
print(my_data_frame.v1.value_counts())

# Lets convert X field which is v1 contains (span or ham) into numeric values.

# my_data_frame['Model_ord'] = pd.Categorical(my_data_frame.v1).codes
# OR ( You can use above line pd.Categorical or my_data_frame.v1.map)
my_data_frame['Model_ord'] = my_data_frame.v1.map({'ham': 0, 'spam': 1})


# # Lets read top 5 records to view our data frame
# print(my_data_frame.head())
#
# # Lets read bottom 5 records to view our data frame
# print(my_data_frame.tail())

# lets populate X and y .
# Remember we want to predict received message is span or ham , so predictive value is always small y and given value
# is always capital X. i.e. sms text is given is X and predictive value is y.
X = my_data_frame['v2'].values
y = my_data_frame['Model_ord'].values

# X.size is 5575 in our case.
# print(X.shape)
# # print(X)
# X = X.reshape(X.size, 1)
# print(X.shape)
# print(X)

# split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# instantiate CountVectorizer (with the default parameters)
vect = CountVectorizer()

# learn the 'vocabulary' of the training data (occurs in-place)
vect.fit(X_train)

# examine the fitted vocabulary
# print(vect.get_feature_names())
# print(vect.vocabulary_)

# transform training data into a 'document-term matrix'
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)
# print(X_train_dtm)
# print("_______________")
# # print sparse matrix to a dense matrix
# print(X_train_dtm.toarray())
# print(type(X_train_dtm))
# print(X_train_dtm.shape)
# print(type(X_train_dtm.toarray()))
# print(X_train_dtm.toarray().shape)
# print(pd.DataFrame(X_train_dtm.toarray(), columns=vect.get_feature_names()).head())


# ################################################################################333
#
# build a model to predict spam or ham. Instantiate the model (with the default parameters)
knn = KNeighborsClassifier(n_neighbors=1)
#
# # fit the model with data (occurs in-place) or train the model.
knn.fit(X_train_dtm, y_train)
#
# # example sms for model testing
simple_test = ["our massage parlor provides full massage by female"]
#
# # transform testing SMS data into a document-term matrix (using existing vocabulary)
simple_test_dtm = vect.transform(simple_test)
simple_test_dtm.toarray()  # check it is required or not.

# examine the vocabulary and document-term matrix together
print(pd.DataFrame(simple_test_dtm.toarray(), columns=vect.get_feature_names()))
#
# predict whether simple_test is spam or ham.
if (knn.predict(simple_test_dtm)) == 0:
	print("this is useful message")
if (knn.predict(simple_test_dtm)) == 1:
	print("this is spam message")


# # ################################################################################333
# Lets Rebuild the same above model using Multinomial Naive bayes model
# ################################################################################333

# instantiate a Multinomial Naive Bayes model
nb = MultinomialNB()

# train the model using X_train_dtm (timing it with an IPython "magic command")
nb.fit(X_train_dtm, y_train)

# make class predictions for X_test_dtm
y_pred_class = nb.predict(X_test_dtm)


# calculate accuracy of class predictions
print(metrics.accuracy_score(y_test, y_pred_class))


# print the confusion matrix
print(metrics.confusion_matrix(y_test, y_pred_class))

# calculate predicted probabilities for X_test_dtm (poorly calibrated)
y_pred_prob = nb.predict_proba(X_test_dtm)[:, 1]
print(y_pred_prob)

# calculate AUC
print(metrics.roc_auc_score(y_test, y_pred_prob))

# ###################################################################################
# Model Comparison - We will compare multinomial Naive Bayes with logistic regression
# ###################################################################################
# logistic regression - despite its name, is a linear model for classification rather
# than regression. Logistic regression is also known in the literature as logit regression,
# maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model,
# the probabilities describing the possible outcomes of a single trial are modeled using
# a logistic function.
# ###################################################################################

# instantiate a logistic regression model
logreg = LogisticRegression()

# train the model using X_train_dtm
logreg.fit(X_train_dtm, y_train)

# make class predictions for X_test_dtm
y_pred_class = logreg.predict(X_test_dtm)

# calculate predicted probabilities for X_test_dtm (well calibrated)
y_pred_prob = logreg.predict_proba(X_test_dtm)[:, 1]
print(y_pred_prob)

# calculate accuracy
metrics.accuracy_score(y_test, y_pred_class)

# calculate AUC
metrics.roc_auc_score(y_test, y_pred_prob)






