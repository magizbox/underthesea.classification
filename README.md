# Vietnamese Text Classification ![](https://img.shields.io/badge/F1-86.7%25-red.svg)

This repository contains experiments in *Vietnamese Text Classification* problem. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.  The code gives an end-to-end working example for reading datasets, training machine learning models, and evaluating performance of the models. It can easily be extended to train your own custom-defined models.

## Table of contents

* [1. Installation](#1-installation)
  * [1.1 Requirements](#11-requirements)
  * [1.2 Download and Setup Environement](#12-download-and-setup-environment)
* [2. Usage](#2-usage)
  * [2.1 Using a pretrained model](#21-using-a-pretrained-model)
  * [2.2 Train a new dataset](#22-train-a-new-dataset)
* [3. References](#3-references)

## 1. Installation

### 1.1 Requirements

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.6+`
* `conda 4+`

### 1.2 Download and Setup Environment

Clone project using git

```
$ git clone https://github.com/undertheseanlp/classification.git
```

Create environment and install requirements

```
$ cd classification
$ conda create -n classification python=3.6
$ pip install -r requirements.txt
```

## 2. Usage

Make sure you are in `classification` folder and activate `classification` environment

```
$ cd classification
$ source activate classification
```

### 2.1 Using a pretrained model


To predict label for a sentence

```
$ python classification.py "Trong suốt kỳ chuyển nhượng mùa hè qua, tiền vệ Eden Hazard của Chelsea đã luôn được Real Madrid nhắm đến để thay thế Cristiano Ronaldo nhưng bất thành. Mới đây, Hazard đã cho biết anh đang chờ đợi thêm những tín hiệu chiêu mộ từ Real Madrid trước khi đưa ra quyết định về tương lai của mình ở Chelsea."
Bong da
```

To predict labels for a file, use option `--fin` and `--fout`

```
$ python classification.py \
    --fin tmp/input.txt
Giao duc
```

### 2.2 Train a new dataset

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

## 3. References

Last update: 10/2018