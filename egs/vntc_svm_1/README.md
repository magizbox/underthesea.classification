# Các thử nghiệm kết hợp mô hình SVM và đặc trưng Tfidf, BoW

Các thử nghiệm được đặt trong mỗi thư mục con của thư mục `egs` bao gồm đầy đủ các thành phần: dữ liệu, mô hình huấn luyện, đánh giá mô hình và việc tối ưu hóa siêu tham số đảm bảo có thể tái sử dụng.

## Mục lục

* [Huấn luyện mô hình](#huấn-luyện-mô-hình)

* [Đánh giá mô hình](#đánh-giá-mô-hình)

* [Tối ưu hóa tham số](#tối-ưu-hóa-tham-số)

Trước khi chạy các thử nghiệm, hãy chắc chắn bạn đã activate môi trường classification, mọi câu lệnh đều được chạy trong thư mục gốc của dự án.
```
$ cd classification/egs/vntc_svm_1
$ source activate classification
```

### Huấn luyện mô hình

Huấn luyện mô hình với dữ liệu `train` đặt tại thư mục `data`.
```
$ python train.py --train data/train.xlsx --s snapshots
```

### Đánh giá mô hình
Đánh giá mô hình với dữ liệu `test` đặt tại thư mục `data`.
```
$ python evaluate.py
```
Kết thúc quá trình đánh giá mô hình sẽ nhận được thông kết quả bao gồm các chỉ số: `accuracy`, `precision`, `recall`, `f1`.

### Tối ưu hóa tham số
Sử dụng Pipeline và GridSearchCV của Sklearn để tối ưu hóa các siêu tham số cho các đặc trưng Tfidf, BoW.

```
$  python optimize_hyperparameters.py 
            --train data/corpus/train.xlsx 
            --test data/corpus/test.xlsx 
            --trans tfidf 
```

```
$ python optimize_hyperparameters.py 
            --train data/corpus/train.xlsx
            --test data/corpus/test.xlsx 
            --trans count
```

Kết thúc quá trình sẽ nhận được bộ tham số tốt nhất cho thử nghiệm. Tham số này sẽ được lưu thành file `json` tại thư mục `experiments` với tên là thử nghiệm tương ứng.

| Thử nghiệm                                      | F1 score (%) |
|-------------------------------------------------|--------------|
| TfidfVectorizer(ngram_range=(1, 2), max_df=0.5) | 92.8         |
| CountVectorizer(ngram_range=(1, 3), max_df=0.5) | 92.0         |

Sử dụng tham số đã được chọn ra để huấn luyện lại và lưu trữ mô hình mới.
```
$ python train.py --train data/corpus/train.xlsx --s snapshots
```