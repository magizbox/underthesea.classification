from sklearn import feature_extraction


class TfidfVectorizer(feature_extraction.text.TfidfVectorizer):
    def __init__(self, default_vocabulary=None, *args, **kwargs):
        super(TfidfVectorizer, self).__init__(*args, **kwargs)
        self.default_vocabulary = default_vocabulary

    def text2vec(self, text):
        return self.fit_transform(text)

    def save(self):
        output = []
        i = 0
        for token in self.vocabulary_:
            output.append({
                "text": token,
                "score": self.idf_[i]
            })
            i += 1
        content = json.dumps(output, ensure_ascii=False)
        open("visualize/features.json", "w").write(content)
