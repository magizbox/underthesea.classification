from os import listdir
from os.path import join
import os
import shutil

baomoi_folder = "/media/anhv/data/projects/ospg-ai/util/ospg-util-common/tmp/baomoi-classification-corpus"
baomoi_corpus_folder = "corpus"
N = 5000
try:
    shutil.rmtree(baomoi_corpus_folder)
except Exception as e:
    raise e
finally:
    os.mkdir(baomoi_corpus_folder)

baomoi_categories = {
    "Đời sống Dinh dưỡng - Làm đẹp": "Làm đẹp và Thể hình - Sức khỏe",
    "Kinh tế Kinh doanh": "Kinh doanh và Công nghiệp",
    "Công nghệ Thiết bị - Phần cứng": "Máy vi tính và Đồ điện tử",
    "Công nghệ": "Máy vi tính và Đồ điện tử - Mạng máy tính và Viễn thông",
    "Kinh tế Tài chính": "Tài chính",
    "Kinh tế Chứng khoán": "Tài chính - Đầu tư - Cổ phiếu và trái phiếu",
    "Văn hóa Ẩm thực": " Văn hóa Ẩm thực",
    "Đời sống Sức khỏe - Y tế": "Sức khoẻ",
    "Nhà đất Không gian - Kiến trúc": "Nhà vườn",
    "Công nghệ CNTT - Viễn thông": "Mạng máy tính và Viễn thông",
    "Giáo dục": "Giáo dục và Việc làm - Giáo dục",
    "Du học": "Giáo dục Học bổng",
    "Thi cử": "Giáo dục Đào tạo",
    "Kinh tế Lao động - Việc làm": "Giáo dục và Việc làm - Việc làm",
    "Pháp luật Hình sự - Dân sự": "Chính trị và Pháp luật",
    "Tin tức": "Xã hội Giao thông",
    "Xã hội": "Con người & Xã hội",
    "Đời sống Tình yêu - Hôn nhân": "Con người & Xã hội - Gia đình & mối quan hệ - Hôn nhân",
    "Văn hóa": "Con người & Xã hội - Khoa học xã hội - Văn hoá",
    "Nhà đất": "Bất động sản",
    "Khoa học": "Khoa học",
    "Xã hội Môi trường - Khí hậu": "Khoa học - Sinh thái & Môi trường",
    "Giải trí Thời trang": "Mua sắm - Trang phục",
    "Thể Thao": "Thể thao",
    "Thể thao Quần vợt": "Thể thao - Thể thao đối kháng",
    "Thể thao Bóng đá quốc tế": "Thể Thao - Thể thao đồng đội - Bóng Đá",
    "Văn hóa Du lịch": "Du lịch"
}
files = listdir(baomoi_folder)
for file in files:
    baomoi_category = file
    if baomoi_category in baomoi_categories:
        category = baomoi_categories[baomoi_category]
        print(category)
        os.mkdir(join(baomoi_corpus_folder, category))
        category_folder = join(baomoi_folder, category)
        posts = listdir(join(baomoi_folder, baomoi_category))
        posts = posts[:N]
        for i, post in enumerate(posts):
            shutil.copyfile(join(baomoi_folder, baomoi_category, post), join(baomoi_corpus_folder, category, post))
            if i > 0 and i % 1000 == 0:
                print(i)
0
