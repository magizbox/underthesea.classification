# Phân loại văn bản tiếng Việt

Dự án này chứa các thử nghiệm trong bài toán *phân loại văn bản tiếng Việt*, là một phần của dự án [underthesea](https://github.com/magizbox/underthesea). Trong đó có chứa mã nguồn cho việc xử lý dữ liệu, huấn luyện và đánh giá các mô hình. Bạn cũng có thể dễ dàng mở rộng để huấn luyện các mô hình trên dữ liệu của riêng mình. 

**Nhóm tác giả** 

* Vũ Anh ([anhv.ict91@gmail.com](anhv.ict91@gmail.com))
* Bùi Nhật Anh ([buinhatanh1208@gmail.com](buinhatanh1208@gmail.com))

Mọi ý kiến đóng góp hoặc yêu cầu trợ giúp xin gửi vào mục [Issues](https://github.com/undertheseanlp/classification/issues) của dự án. Các thảo luận được khuyến khích **sử dụng tiếng Việt** để dễ dàng trong quá trình trao đổi. 

## Mục lục

* [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
* [Thiết lập môi trường](#thiết-lập-môi-trường)
* [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
  * [Sử dụng mô hình đã huấn luyện sẵn](#sử-dụng-mô-hình-đã-huấn-luyện-sẵn)
  * [Huấn luyện mô hình mới](#huấn-luyện-mô-hình-mới) 
* [Trích dẫn](#trích-dẫn)


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


To predict label for a sentence

```
$ python classification.py "Trong suốt kỳ chuyển nhượng mùa hè qua, tiền vệ Eden Hazard của Chelsea đã luôn được Real Madrid nhắm đến để thay thế Cristiano Ronaldo nhưng bất thành. Mới đây, Hazard đã cho biết anh đang chờ đợi thêm những tín hiệu chiêu mộ từ Real Madrid trước khi đưa ra quyết định về tương lai của mình ở Chelsea."
Bong da
```

To predict labels from file, use option `--fin`

```
$ python classification.py \
    --fin tmp/input.txt
Giao duc
```

### Huấn luyện mô hình mới

**Prepare a new dataset**

Convert your dataset to excel file.

```
$ python util/preprocess.py
```

**Benchmark experiments**

```
# experiments using linearSVC and tfidfvectorizer
$ python benchmark.py --mode benchmark 
            --train data/corpus/train.xlsx 
            --test data/corpus/test.xlsx 
            --transform tfidf 
            --s report/benchmark_model_tfidf.png
```
```
# experiments using linearSVC and countvectorizer
$ python benchmark.py --mode benchmark 
            --train data/corpus/train.xlsx
            --test data/corpus/test.xlsx 
            --transform count 
            --s report/benchmark_model_count.png
```


**Train and save model**

```
$ python train.py --mode train-test 
            --train data/corpus/train.xlsx 
            --test data/corpus/test.xlsx 
            --train_size 0.2 
            --s models
```

## Trích dẫn

Last update: 10/2018
