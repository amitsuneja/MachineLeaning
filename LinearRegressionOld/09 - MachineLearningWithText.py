# https://www.youtube.com/watch?v=vTaxdJ6VYWE
# load the iris dataset as an example
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Part 1: Model building in scikit-learn (refresher)


iris = load_iris()
# store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

print(iris.feature_names)
# check the shapes of X and y
print(X.shape)
print(y.shape)
print(X)
print(pd.DataFrame(X, columns=iris.feature_names).head())

# examine the response vector
print(y)

# instantiate the model (with the default parameters)
kneighbour = KNeighborsClassifier()

# fit the model with data (occurs in-place)
kneighbour.fit(X, y)

# predict the response for a new observation
print("Predicted Value of y = ", kneighbour.predict([[3, 5, 4, 2]]))

# Part 2: Representing text as numerical data

# example text for model training (SMS messages)
simple_train = ['call you tonight', 'Call me a cab', 'please call me... PLEASE!']

# example response vector
is_desperate = [0, 0, 1]

# import and instantiate CountVectorizer (with the default parameters)
vect = CountVectorizer()

# learn the 'vocabulary' of the training data (occurs in-place)
vect.fit(simple_train)

# examine the fitted vocabulary
print(vect.get_feature_names())
print("________________________________________________________")

# transform training data into a 'document-term matrix'
simple_train_dtm = vect.transform(simple_train)
print(type(simple_train_dtm))
print(simple_train_dtm.shape)

# convert sparse matrix to a dense matrix
print(simple_train_dtm.toarray())

# examine the vocabulary and document-term matrix together
print(pd.DataFrame(simple_train_dtm.toarray(), columns=vect.get_feature_names()))

# check the type of the document-term matrix
print(type(simple_train_dtm))

# examine the sparse matrix contents
print(simple_train_dtm)

# build a model to predict desperation
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(simple_train_dtm, is_desperate)

# example text for model testing
simple_test = ["please call"]

# transform testing data into a document-term matrix (using existing vocabulary)
simple_test_dtm = vect.transform(simple_test)
print(simple_test_dtm.toarray())

# examine the vocabulary and document-term matrix together
print(pd.DataFrame(simple_test_dtm.toarray(), columns=vect.get_feature_names()))


# predict whether simple_test is desperate
print(knn.predict(simple_test_dtm))