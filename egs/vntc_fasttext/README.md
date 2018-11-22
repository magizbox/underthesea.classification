# Thử nghiệm với Fasttext
## Kết quả

Kết quả trên tập test với tham số mặc định

```
Load model time: 0.190s
Accuracy: 0.8681
Precision: 0.8681
Recall   : 0.8681
Micro F1 : 0.8681
Predict time: 4.618s
```



## Hướng dẫn sử dụng

### Khởi tạo dữ liệu
```
$ python preprocess.py
```

### Huấn luyện mô hình 

```
python train.py --train data/train.txt --s snapshots 
```

### Đánh giá mô hình 

```
 python evaluate.py --test data/test.txt --s snapshots 
```