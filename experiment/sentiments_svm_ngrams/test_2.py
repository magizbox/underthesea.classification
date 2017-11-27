from unittest import TestCase
from model import sentiment


class TestSentiment(TestCase):
    def test_sentiment(self):
        sentences = ["Thật tuyệt vời"]
        tags = "POSITIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_1(self):
        sentences = ["Nhân viên BIDV dễ thương nhiệt tình lắm ạ"]
        tags = "POSITIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_2(self):
        sentences = ["Không tin tưởng vào ngân hàng BIDV."]
        tags = "NEGATIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_3(self):
        sentences = ["Dịch vụ rắc rối."]
        tags = "NEGATIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_4(self):
        sentence = "Thật sự mình rất hài lòng khi làm việc với VietcomBank"
        actual = sentiment(sentence)
        expected = ("NEGATIVE")
        self.assertEquals(expected, actual)

    def test_sentiment_5(self):
        sentences = ["Vietcombank là lũ lừa đảo"]
        tags = "NEGATIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_6(self):
        sentences = ["Đkmm"]
        tags = "NEGATIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)

    def test_sentiment_7(self):
        sentences = ["éo tin"]
        tags = "NEGATIVE"
        actual = "".join(sentiment(sentences[0]))
        self.assertEquals(tags, actual)
