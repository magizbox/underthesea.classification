# Phân loại văn bản tiếng Việt

![](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)
![](https://img.shields.io/badge/opensource-vietnamese-blue.svg)
![](https://img.shields.io/badge/build-passing-green.svg)

Dự án nghiên cứu về bài toán *phân loại văn bản tiếng Việt*, được phát triển bởi nhóm nghiên cứu xử lý ngôn ngữ tự nhiên tiếng Việt - [underthesea](https://github.com/undertheseanlp). Chứa mã nguồn các thử nghiệm cho việc xử lý dữ liệu, huấn luyện và đánh giá mô hình, cũng như cho phép dễ dàng tùy chỉnh mô hình đối với những tập dữ liệu mới.

**Nhóm tác giả** 

* Vũ Anh ([anhv.ict91@gmail.com](anhv.ict91@gmail.com))
* Bùi Nhật Anh ([buinhatanh1208@gmail.com](buinhatanh1208@gmail.com))
* Mai Duy Khánh ([khanh.md01@gmail.com](khanh.md01@gmail.com))

**Tham gia đóng góp**

Mọi ý kiến đóng góp hoặc yêu cầu trợ giúp xin gửi vào mục [Issues](../../issues) của dự án. Các thảo luận được khuyến khích **sử dụng tiếng Việt** để dễ dàng trong quá trình trao đổi. 

Nếu bạn có kinh nghiệm trong bài toán này, muốn tham gia vào nhóm phát triển với vai trò là [Developer](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor), xin hãy đọc kỹ [Hướng dẫn tham gia](https://github.com/undertheseanlp/underthesea/wiki/H%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-%C4%91%C3%B3ng-g%C3%B3p#developercontributor).

**Lời cảm ơn**

Xin chân thành cảm ơn các nhóm phát triển sklearn, fasttext đã tạo ra những công cụ hữu ích để nhóm sử dụng trong các thử nghiệm của mình.

## Mục lục

* [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
* [Thiết lập môi trường](#thiết-lập-môi-trường)
* [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
  * [Sử dụng mô hình đã huấn luyện](#sử-dụng-mô-hình-đã-huấn-luyện)
  * [Huấn luyện mô hình](#huấn-luyện-mô-hình) 
* [Kết quả thử nghiệm](#kết-quả-thử-nghiệm)
* [Trích dẫn](#trích-dẫn)
* [Bản quyền](#bản-quyền)


## Yêu cầu hệ thống 

* `Hệ điều hành: Linux (Ubuntu, CentOS), Mac`
* `Python 3.6+`
* `conda 4+`

## Thiết lập môi trường

Tải project bằng cách sử dụng lệnh `git clone`

```
$ git clone https://github.com/undertheseanlp/classification.git
```

Tạo môi trường mới và cài đặt các gói liên quan

```
$ cd classification
$ conda create -n classification python=3.6
$ pip install -r requirements.txt
```

## Hướng dẫn sử dụng

Trước khi chạy các thử nghiệm, hãy chắc chắn bạn đã activate môi trường `classification`, mọi câu lệnh đều được chạy trong thư mục gốc của dự án.

```
$ cd classification
$ source activate classification
```

### Sử dụng mô hình đã huấn luyện sẵn


Dự đoán nhãn của một câu:

```
$ python classification.py "Trong suốt kỳ chuyển nhượng mùa hè qua, tiền vệ Eden Hazard của Chelsea đã luôn được Real Madrid nhắm đến để thay thế Cristiano Ronaldo nhưng bất thành. Mới đây, Hazard đã cho biết anh đang chờ đợi thêm những tín hiệu chiêu mộ từ Real Madrid trước khi đưa ra quyết định về tương lai của mình ở Chelsea."
Bong da
```

Dự đoán nhãn từ nội dung trong file, sử dụng tùy chọn `--fin`

```
$ python classification.py \
    --fin tmp/input.txt
Giao duc
```

### Huấn luyện mô hình

**Chuẩn bị tập dữ liệu mới**

Chuyển đổi tập dữ liệu của bạn thành file excel

```
$ python util/preprocess.py
```

**So sánh các thử nghiệm**

Các thử nghiệm kết hợp linearSVC và Tfidfvectorizer/Countvectorizer

```
$ python benchmark.py --mode benchmark 
            --train data/corpus/train.xlsx 
            --test data/corpus/test.xlsx 
            --transform tfidf 
            --s report/benchmark_model_tfidf.png
```
```
$ python benchmark.py --mode benchmark 
            --train data/corpus/train.xlsx
            --test data/corpus/test.xlsx 
            --transform count 
            --s report/benchmark_model_count.png
```


**Huấn luyện và lưu mô hình**

```
$ python train.py --mode train-test 
            --train data/corpus/train.xlsx 
            --test data/corpus/test.xlsx 
            --train_size 0.2 
            --s models
```

## Kết quả thử nghiệm 
Mô tả dữ liệu VNTC
| Label                | Topic                | Train  | Test   |
|----------------------|----------------------|--------|--------|
| am_nhac              | Âm Nhạc              | 900    | 813    |
| am_thuc              | Ẩm thực              | 265    | 400    |
| bat_dong_san         | Bất động sản         | 246    | 282    |
| bong_da              | Bóng đá              | 1,857  | 1,464  |
| chung_khoan          | Chứng khoán          | 382    | 320    |
| cum_ga               | Cúm gà               | 510    | 381    |
| cuoc_song_do_day     | Cuộc sống đó đây     | 729    | 405    |
| du_hoc               | Du học               | 682    | 394    |
| du_lich              | Du lịch              | 582    | 565    |
| duong_vao_WTO        | Đường vào WTO        | 208    | 191    |
| gia_dinh             | Gia đình             | 213    | 280    |
| giai_tri_tin_hoc     | Giải trí tin học     | 825    | 707    |
| giao_duc             | Giáo dục             | 821    | 707    |
| gioi_tinh            | Giới tính            | 343    | 268    |
| hacker_&_virus       | Hacker & Virus       | 355    | 319    |
| hinh_su              | Hình sự              | 155    | 196    |
| khong_gian_song      | Không gian sống      | 134    | 58     |
| kinh_doanh_quoc_te   | Kinh doanh quốc tế   | 571    | 559    |
| lam_dep              | Làm đẹp              | 776    | 735    |
| loi_song             | Lối sống             | 223    | 214    |
| mua_sam              | Mua sắm              | 187    | 84     |
| my_thuat             | Mỹ thuật             | 193    | 144    |
| san_khau_dien_anh    | Sân khấu điện ảnh    | 1,117  | 1,030  |
| san_pham_tin_hoc_moi | Sản phẩm tin học mới | 770    | 595    |
| tennis               | Tennis               | 588    | 283    |
| the_gioi_tre         | Thế giới trẻ         | 331    | 380    |
| thoi_trang           | Thời trang           | 412    | 302    |
|                      | Tổng kết             | 14,375 | 12,076 |

Kết quả thử nghiệm trên tập dữ liệu VNTC 

| Mô hình                                         | F1 % |
|-------------------------------------------------|------|
| TfidfVectorizer(max_df=0.8)                     | 83.0 |
| TfidfVectorizer(max_df=0.6)                     | 86.6 |
| TfidfVectorizer(max_df=0.5)                     | 86.7 |
| CountVectorizer(ngram_range=(1, 2), max_df=0.6) | 87.6 |
| CountVectorizer(ngram_range=(1, 2), max_df=0.5) | 87.7 |
| CountVectorizer(ngram_range=(1, 2))             | 88.2 |

## Trích dẫn

Nếu bạn thấy mã nguồn này hữu ích, xin hãy trích dẫn đường dẫn của dự án trong các nghiên cứu của mình 

```
@online{undertheseanlp/classification,
author ={Vu Anh, Bui Nhat Anh},
year = {2018},
title ={Phân loại văn bản tiếng Việt},
url ={https://github.com/undertheseanlp/classification}
}
```

## Bản quyền

Mã nguồn của dự án được phân phối theo giấy phép [GPL-3.0](LICENSE.txt).

Dự án sử dụng tập dữ liệu **[VNTC](https://github.com/duyvuleo/VNTC)** trong các thử nghiệm. Xin vui lòng kiểm tra lại thông tin trên website hoặc báo cáo khoa học tương ứng để biết thông tin về bản quyền và trích dẫn khi sử dụng tập dữ liệu này. 
