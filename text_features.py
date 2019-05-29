from sklearn.base import BaseEstimator, TransformerMixin
import string
from underthesea.word_tokenize.regex_tokenize import tokenize


class Lowercase(BaseEstimator, TransformerMixin):
    def transform(self, x):
        return [s.lower() for s in x]

    def fit(self, x, y=None):
        return self


class Tokenize(BaseEstimator, TransformerMixin):
    def pun_num(self, s):
        for token in s.split():
            if token in string.punctuation:
                if token == '.':
                    s = s
                else:
                    s = s.replace(token, 'punc')
            else:
                s = s
        return s

    def transform(self, x):
        return [self.pun_num(tokenize(s, format='text')) for s in x]

    def fit(self, x, y=None):
        return self
