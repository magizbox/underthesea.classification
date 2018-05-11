import fasttext

train_data = "data_fasttext/vn.news.train.txt"
classifier = fasttext.supervised(train_data, 'model')

sentences_lives = [
    "Đã truy ra nguồn gốc loại đinh lạ trên cao tốc Bắc Giang - Hà Nội",
    "Tự ý tháo dỡ hàng rào cố định bảo vệ hành lang cầu Nhật Tân",
    "Dân khốn khổ vì tài xế đua nhau né trạm BOT quốc lộ 5",
    "Lội qua suối đi làm, một người phụ nữ bị cuối trôi"
]

sentences_sports = [
    "“Thể lực thua kém, đội tuyển Việt Nam thật may khi không thua Campuchia”"
]


print("\nXa Hoi")
print(classifier.predict(sentences_lives))

print("\nThe Thao")
print(classifier.predict(sentences_sports))

