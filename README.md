# Vietnamese Text Classification ![](https://img.shields.io/badge/F1-86.7%25-red.svg)

This repository contains experiments in Vietnamese Text Classification problems. It is a part of [underthesea](https://github.com/magizbox/underthesea) project.

## Table of contents

* [1. Installation](#1.-installation)
  * [1.1 Requirements](#1.1-requirements)
  * [1.2 Download and Setup Environement](#1.2-download-and-setup-environment)
* [2. Usage](#2.-usage)
  * [2.1 Using a pretrained model](#2.1-using-a-pretrained-model)
  * [2.2 Train a new dataset](#2.2-train-a-new-dataset)
  * [2.3 Sharing a model](#2.3-sharing-a-model)
* [3. References](#3.-references)

## 1. Installation

### 1.1 Requirements

* `Operating Systems: Linux (Ubuntu, CentOS), Mac`
* `Python 3.5+`
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
$ conda create -n classification python=3.5
$ pip install -r requirements.txt
```

## 2. Usage

### 2.1 Using a pretrained model

```
cd classification
$ source activate classification
$ python classication.py -fin tmp/input.txt -fout tmp/output.txt
```

### 2.2 Train a new dataset

**Prepare a new dataset**

To be updated

**Train and test**

```
$ cd classification
$ source activate classification
$ python classication.py
  --train data/vlsp2018/corpus/train.txt
```

### 2.3 Sharing a model

To be updated

## 3. References

* Detail Reports, [link](https://docs.google.com/spreadsheets/d/1PUnNBVywHbG4fpqSzBAV6jPWFNOKaiIQEKWM-W2mxiE/edit?usp=sharing)
* Vietnamese Text Classification publications, [link](https://github.com/magizbox/underthesea/wiki/Vietnamese-NLP-Publications#text-classification)

Last update: 05/2018