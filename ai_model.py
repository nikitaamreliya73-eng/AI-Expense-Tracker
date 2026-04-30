<<<<<<< HEAD
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "pizza burger food zomato swiggy",
    "uber ola taxi bus travel ride",
    "netflix movie cinema entertainment",
    "amazon flipkart shopping clothes",
]

labels = [
    "Food",
    "Travel",
    "Entertainment",
    "Shopping"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(text):
    return model.predict(vectorizer.transform([text]))[0]
=======
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "pizza burger food swiggy zomato",
    "dinner lunch restaurant food",
    "uber ola taxi bus train ride travel",
    "movie netflix cinema youtube entertainment",
    "amazon flipkart shopping clothes mall",
    "petrol diesel fuel bike car transport"
]

labels = [
    "Food",
    "Food",
    "Travel",
    "Entertainment",
    "Shopping",
    "Transport"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]
>>>>>>> cf4a782663c4ad0b009758a3bb656d3c6ff35356
