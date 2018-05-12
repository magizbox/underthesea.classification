from os.path import join
import os
import fasttext
from util.convert_to_fasttext_classification_corpus import convert_to_fasttext_classification_corpus

path = os.path.abspath("./data/TC201805/corpus")
convert_to_fasttext_classification_corpus(path, "tmp/train.txt")

classifier = fasttext.supervised('tmp/train.txt', 'tmp/model.bin')
sentences = [
    'Tôi bị Phạm Anh Khoa khóa tay, ép vào tường để tấn công tình dục',
    'Người Thái cử thêm 3 nhân sự vào Bia Sài Gòn',
    'Salah dập tắt tham vọng của Real Madrid',
    'Tottenham có vé Champions League, đẩy Liverpool xuống thứ tư',
    'Nadal phá kỷ lục tồn tại 34 năm, gặp Thiem ở tứ kết Madrid Mở rộng',
    'Diễn biến ngày đầu The Players Championship',
    'Xuân Trường lọt top 5 bàn thắng đẹp nhất vòng 7 V-League 2018'
]

print(classifier.predict(sentences))
