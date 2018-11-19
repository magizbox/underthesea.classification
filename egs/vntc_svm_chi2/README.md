# Thử nghiệm với SVM

## Kết quả

Kết quả trên tập test

```
Accuracy: 0.918
Precision: 0.918
Recall: 0.918
F1 Score: 0.918 
```

Tham số: CountVectorizer(ngram_range=(1, 2), max_df=0.7)

```
Load model time: 2.467s
Predict time: 59.249s
Accuracy: 0.915
Precision: 0.915
Recall: 0.915
F1 Score: 0.915
```



## Hướng dẫn sử dụng

### Huấn luyện mô hình 

```
python train.py --train data/train.xlsx -s snapshots 
```

### Đánh giá mô hình 

```
python evaluate.py 
```

### Dự đoán

```
python predict.py 
```

