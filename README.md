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

Python Packages

* `underthesea==1.1.7`
* `languageflow==1.1.7`

### 1.2 Download and Setup Environment

Clone project using git

```
$ git clone https://github.com/undertheseanlp/classification.git
```

Create environment and install requirements

```
$ cd ner
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
$ python classification.py "Tái phát chấn thương, Neymar không thể tập luyện"
'the_thao'
```

To predict labels for a file, use option `--fin` and `--fout`

```
$ python classification.py \
    --fin tmp/input.txt \
    --fout tmp/output.txt
```

### 2.2 Train a new dataset

**Prepare a new dataset**

Convert your dataset to [Underthesea Text Classification Data Format](https://github.com/undertheseanlp/classification/blob/master/data_format.md)

Example

```
__label__giao_duc Bất ngờ tranh luận quanh bìa SGK Lịch sử lớp 7 có hình Vạn Lý Trường Thành
__label__giao_duc Tuyển sinh lớp 10 năm 2019 của Hà Nội: Chọn phương án nào hữu hiệu?
__label__giao_duc Hơn 122.000 giáo viên mầm non nghỉ công tác chưa được hưởng chế độ
__label__the_thao Báo chí Đông Nam Á hết mực khen ngợi Olympic Việt Nam
__label__the_thao “Không nên để Công Phượng tiếp tục đá phạt đền!”
__label__the_thao Chia tay Tottenham, ngôi sao Son Heung-min về thi đấu ở Asiad 2018
```

**Train and test**

```
$ python util/preprcess_vntc.py
$ python train.py --mode train-test \
     --train tmp/vntc/train.txt \
     --test tmp/vntc/test.txt
```

**Train and save model**

```
$ python train.py --mode train \
     --train data/VNTC/corpus/train \
     --s tmp/model.bin 
```

## 3. References

Last update: 08/2018