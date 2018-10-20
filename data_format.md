# Mô tả dữ liệu

| Phiên bản         | v1.0.0     |
|-------------------|------------|
| Lần cập nhật cuối | 20/10/2018 |
| Người thực hiện   | Bùi Nhật Anh     |

Tài liệu mô tả đề xuất về cấu trúc chuẩn của tập dữ liệu (corpus) đối với bài toán phân loại văn bản (text classification). Được áp dụng trong các thí nghiệm của [`underthesea`](http://github.com/undertheseanlp/classification) từ phiên bản 1.2.0.


### Tập dữ liệu

Dữ liệu của bài toán phân loại văn bản được lưu trong thư mục `data`, gồm hai thư mục con `raw` và `corpus`.

* Dữ liệu thô được lưu trong thư mục `raw` bao gồm hai thư mục con `train` và `test`.
* Dữ liệu huấn luyện và kiểm thử được lưu trong thư mục `corpus`.

Cấu trúc thư mục

```
.
├── raw
|   ├── train
|   |   ├── Am nhac
|   |   ├── Am thuc
|   |   ├── Bat dong san
|   |   └── ...
|   └── test
|   |   ├── Am nhac
|   |   ├── Am thuc
|   |   ├── Bat dong san
|   |   └── ...
└── corpus
    ├── train.xlsx
    └── test.xlsx
```

Thư mục `raw` chứa dữ liệu [`VNTC`](https://github.com/duyvuleo/VNTC) bao gồm hai thư mục `train` và `test`, mỗi thư mục gồm 27 thư mục, mỗi thư mục gồm các file văn bản (với đuôi định dạng txt). File `text` chứa nội dung của từng văn bản ứng với tên file tương ứng.

*Format*: `<text_file_id>|<text content>`

*Ví dụ trong thư mục `Am nhac`*
```
AN_NLD_T_ (761)|text content 761
AN_NLD_T_ (762)|text content 762
AN_NLD_T_ (763)|text content 763
AN_NLD_T_ (764)|text content 764
```
Tương tự như vậy với 26 thư mục còn lại.

**Phân phối file văn bản trong bộ dữ liệu**

| Topic                | Train  | Test   |
|----------------------|--------|--------|
| Am nhac              | 900    | 813    |
| Am thuc              | 265    | 400    |
| Bat dong san         | 246    | 282    |
| Bong da              | 1,857  | 1,464  |
| Chung khoan          | 382    | 320    |
| Cum ga               | 510    | 381    |
| Cuoc song do day     | 729    | 405    |
| Du hoc               | 682    | 394    |
| Du lich              | 582    | 565    |
| Duong vao WTO        | 208    | 191    |
| Gia dinh             | 213    | 280    |
| Giai tri tin hoc     | 825    | 707    |
| Giao duc             | 821    | 707    |
| Gioi tinh            | 343    | 268    |
| Hacker & Virus       | 355    | 319    |
| Hinh su              | 155    | 196    |
| Khong gian song      | 134    | 58     |
| Kinh doanh quoc te   | 571    | 559    |
| Lam dep              | 776    | 735    |
| Loi song             | 223    | 214    |
| Mua sam              | 187    | 84     |
| My thuat             | 193    | 144    |
| San khau dien anh    | 1,117  | 1,030  |
| San pham tin hoc moi | 770    | 595    |
| Tennis               | 588    | 283    |
| The gioi tre         | 331    | 380    |
| Thoi trang           | 412    | 302    |
| **Tổng kết**         | 14,375 | 12,076 |

Thư mục `corpus` chứa dữ liệu huấn luyện và kiểm thử tương tự với 2 file `train.xlsx` và `test.xlsx`. Để có được 2 file này, chạy câu lệnh:
```
$ python preprocess_vntc.py
```
Mỗi văn bản trong bộ dữ liệu VNTC được biến đổi dạng one-hot-coding và lưu trữ trong file excel.

*Ví dụ*

| text                                                                          | am_nhac | am_thuc | bat_dong_san | bong_da |
|-------------------------------------------------------------------------------|---------|---------|--------------|---------|
| UBND TP Hà Nội vừa ban hành quyết định về giá bán căn hộ chung cư cao tầng... | 0       | 0       | 1            | 0       |
| Hồ Ngọc Hà: 'Đôi khi tôi hơi coi thường đàn ông' ...                          | 1       | 0       | 0            | 0       |
| Riquelme vắng mặt trận gặp M.U                                                | 0       | 0       | 0            | 1       |
| Các quán tiết canh Hà Nội giờ đóng cửa                                        | 0       | 1       | 0            | 0       |

Với 2 thư mục `train` và `test` sẽ thu được 2 file `train.xlsx` và `test.xlsx` tương ứng.