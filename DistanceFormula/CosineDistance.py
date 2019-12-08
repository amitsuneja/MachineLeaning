from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

my_text_corpus = [
 'the brown fox jumped over the brown dog',
 'the quick brown brown brown fox',
 'the brown dog',
 'the fox ate the dog'
]

query = ["brown"]
X = vectorizer.fit_transform(my_text_corpus)
Y = vectorizer.transform(query)
print(vectorizer.get_feature_names())
print(X.toarray())
print(Y)
print(cosine_similarity(Y, X.toarray()))  # [0.54267123 0.82814363 0.61217198 0.        ]]

# As you can see from the above example, we queried for word “brown” and in corpus
# there are only three documents which contain word “brown”. When checked with cosine
# similarity metric it gave the same results by having >0 values for three document
# except the forth one.