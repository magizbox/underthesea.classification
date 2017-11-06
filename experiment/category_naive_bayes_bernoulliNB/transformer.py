from sklearn import feature_extraction


class TfidfVectorizer(feature_extraction.text.TfidfVectorizer):
    def __init__(self, default_vocabulary=None, *args, **kwargs):
        super(TfidfVectorizer, self).__init__(*args, **kwargs)
        self.default_vocabulary = default_vocabulary

    def text2vec(self, text):
        return self.fit_transform(text)
