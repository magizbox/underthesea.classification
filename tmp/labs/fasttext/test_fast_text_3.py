from model.fasttext import FastTextPredictor

X = [
    "Thu phí BOT kiểu trấn lột: Trả một đồng mà bất công, dân cũng không chịu!",
    "Mực sống đang bơi tung tăng 1 triệu đồng/kg về Hà Nội cháy hàng",
    "Con gái \"Rambo\" Sylvester Stallone quyến rũ đi xem thời trang",
    "So gia sản kếch xù nhà chồng hai gái ngoan đình đám nhất showbiz Việt",
    "Phó Giám đốc ĐHQG Hà Nội: “Các trường đại học nên đón nhận văn hóa xếp hạng”",
    "Hiệu trưởng trường chất lượng cao xin nghỉ việc khi bị điều động về Sở Giáo dục",
    "Hội chứng hiếm khiến tim bé trai ngừng đập khi ăn xúc xích",
    "SpaceX phóng thành công máy bay bí mật của không quân Mỹ",
    "Nhan sắc thí sinh sơ khảo Hoa hậu Hoàn vũ VN phía Bắc",
    "Đàn cá mập hàng trăm con thưởng thức 'đại tiệc' cá ngừ",
    # "Cát Phượng: 'Tôi chẳng có gì để chồng trẻ lợi dụng'  30 Cát Phượng: Diễn viên cho biết chị không giúp đỡ nhiều cho Kiều Minh Tuấn trong nghề nghiệp vì anh tự lập và đủ khôn ngoan. "
    "Messi thật tội nghiệp khi phải thi đấu với những con lừa",
    # "chó",
    "Bill Gates mua điện thoại sử dụng hệ điều hành iOS",
    # "máy tính chậm thế"
]

predictor = FastTextPredictor.Instance()
print(predictor.predict(X))
