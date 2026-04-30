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