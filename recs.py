from sklearn.feature_extraction.text import CountVectorizer

doc0 = "hello world"
doc1 = "foo bar"
doc2 = "lottery prize winner"
docs_train = [doc0] * 100 + [doc1] * 100 + [doc2] * 4

docs_test = [
             "lottery winner",
             "hello foo",
             "hello bar",
             "lottery prize",
             "world foo",
             "prize winner",
            ]

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(docs_train).toarray()
features = vectorizer.get_feature_names()







