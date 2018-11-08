# Mô tả dữ liệu

| Phiên bản         | v1.0.1     |
|-------------------|------------|
| Lần cập nhật cuối | 06/11/2018 |
| Người thực hiện   | Bùi Nhật Anh     |

Tài liệu mô tả đề xuất về cấu trúc chuẩn của tập dữ liệu (corpus) đối với bài toán phân loại văn bản (text classification). Được áp dụng trong các thí nghiệm của [`underthesea`](http://github.com/undertheseanlp/classification).


### Tập dữ liệu

Dữ liệu của bài toán phân loại văn bản được lưu trong thư mục `data`, gồm hai thư mục con `raw` và `corpus`.

* Dữ liệu thô được lưu trong thư mục `raw` bao gồm hai thư mục con `train` và `test`.
* Dữ liệu huấn luyện và kiểm thử được lưu trong thư mục `corpus`.

Cấu trúc thư mục

```
.
├── raw
|   ├── Train_Full
|   |   ├── Chinh tri Xa hoi
|   |   ├── Doi song
|   |   ├── Khoa hoc
|   |   └── ...
|   └── Test_Full
|   |   ├── Chinh tri Xa hoi
|   |   ├── Doi song
|   |   ├── Khoa hoc
|   └── └── ...
└── corpus
    ├── train.xlsx
    └── test.xlsx
```

Thư mục `raw` chứa dữ liệu [`VNTC`](https://github.com/duyvuleo/VNTC) bao gồm 33759 văn bản cho việc huấn luyện, 50373 văn bản cho việc kiểm thử, tương ứng với hai thư mục `train` và `test`, mỗi thư mục gồm 10 thư mục với 10 topic của bộ dữ liệu, mỗi thư mục gồm các file văn bản (với đuôi định dạng txt). File `text` chứa nội dung của từng văn bản ứng với tên file tương ứng.

*Format*: `<text_file_id>|<text content>`

*Ví dụ trong thư mục `Chinh tri Xa hoi`*
```
XH_NLD_ (3672)|text content 3672
XH_NLD_ (3673)|text content 3673
XH_NLD_ (3674)|text content 3674
XH_NLD_ (3675)|text content 3675
```
Tương tự như vậy với 9 thư mục còn lại.
 

Thư mục `corpus` chứa dữ liệu huấn luyện và kiểm thử tương tự với 2 file `train.xlsx` và `test.xlsx`. Để có được 2 file này, chạy câu lệnh:
```
$ python preprocess_vntc.py
```
Mỗi văn bản trong bộ dữ liệu VNTC được biến đổi dạng one-hot-coding và lưu trữ trong file excel.

*Ví dụ*

| text                                                                          | chnh_tri_xa_hoi| doi_song |khoa_hoc| kinh_doanh|
|-------------------------------------------------------------------------------|---------|---------|--------------|---------|
|thành lập dự án policy phòng chống hiv/aids ở vn...| 1  | 0       | 0            | 0       |
|  sử dụng màu sắc trong trang trí nội thất ...                          | 0       | 1       | 0            | 0       |
| sếu đầu đỏ ở vườn quốc gia tràm chim vườn quốc gia tràm chim...                                             | 0       | 0       | 1           | 0       |
|  không thu thuế đối với các loại trái phiếu chính phủ ...                                     | 0       | 0       | 0            | 1       |

Với 2 thư mục `train` và `test` sẽ thu được 2 file `train.xlsx` và `test.xlsx` tương ứng.
