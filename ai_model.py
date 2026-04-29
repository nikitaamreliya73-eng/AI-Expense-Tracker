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