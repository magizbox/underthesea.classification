# Hướng dẫn 

Bước 1: Cài đặt SRILM

1.1 Vào địa chỉ [http://www.speech.sri.com/projects/srilm/download.html](http://www.speech.sri.com/projects/srilm/download.html) để tải `srilm-1.7.2.tar.gz`

1.2 Chạy các dòng lệnh sau

```
mkdir /usr/share/srilm
mv srilm-1.7.2.tar.gz /usr/share/srilm/
cd /usr/share/srilm
tar xvf srilm-1.7.2.tar.gz
```

1.3 Chỉnh sửa cấu hình

Mở file `Makefile`, đổi dòng thứ 7 có nội dung `# SRILM = /home/speech/stolcke/project/srilm/devel` thành

```
SRILM = /usr/share/srilm
```

1.4 Chạy các dòng lệnh sau

```
sudo tcsh
sudo make NO_TCL=1 MACHINE_TYPE=i686-m64 World
sudo ./bin/i686-m64/ngram-count -help
```

Bước 2: Chạy thử SRILM

1. Tạo file `corpus.txt` với nội dung

```
tôi đi học
tôi rất vui
tôi đi chơi
```

2. Tạo file `test.txt` với nội dung

```
học mà chơi
học rất vui
tôi chơi rất vui 
```

3. Huấn luyện mô hình ngôn ngữ 

```
$ bin/i686-m64/ngram-count -text corpus.txt -lm lm.lm -order 2
warning: discount coeff 1 is out of range: 0
warning: count of count 8 is zero -- lowering maxcount
warning: count of count 7 is zero -- lowering maxcount
warning: count of count 6 is zero -- lowering maxcount
warning: count of count 5 is zero -- lowering maxcount
warning: count of count 4 is zero -- lowering maxcount
warning: discount coeff 1 is out of range: -0.25
warning: discount coeff 2 is out of range: 1.875
```

4. Sử dụng mô hình ngôn ngữ

```
$ bin/i686-m64/ngram -lm lm.lm -order 2 -ppl test.txt -debug 2 
reading 8 1-grams
reading 9 2-grams
học mà chơi
	p( học | <s> ) 	= [1gram] 0.02777779 [ -1.556302 ]
	p( <unk> | học ...) 	= [OOV] 0 [ -inf ]
	p( chơi | <unk> ...) 	= [1gram] 0.08333339 [ -1.079181 ]
	p( </s> | chơi ...) 	= [2gram] 0.5 [ -0.30103 ]
1 sentences, 3 words, 1 OOVs
0 zeroprobs, logprob= -2.936513 ppl= 9.524403 ppl1= 29.39386

học rất vui
	p( học | <s> ) 	= [1gram] 0.02777779 [ -1.556302 ]
	p( rất | học ...) 	= [1gram] 0.05555559 [ -1.255272 ]
	p( vui | rất ...) 	= [2gram] 0.5 [ -0.30103 ]
	p( </s> | vui ...) 	= [2gram] 0.5 [ -0.30103 ]
1 sentences, 3 words, 0 OOVs
0 zeroprobs, logprob= -3.413635 ppl= 7.135241 ppl1= 13.73657

tôi chơi rất vui
	p( tôi | <s> ) 	= [2gram] 0.7500001 [ -0.1249387 ]
	p( chơi | tôi ...) 	= [1gram] 0.0277778 [ -1.556302 ]
	p( rất | chơi ...) 	= [1gram] 0.05555559 [ -1.255272 ]
	p( vui | rất ...) 	= [2gram] 0.5 [ -0.30103 ]
	p( </s> | vui ...) 	= [2gram] 0.5 [ -0.30103 ]
1 sentences, 4 words, 0 OOVs
0 zeroprobs, logprob= -3.538573 ppl= 5.101697 ppl1= 7.667315

file test.txt: 3 sentences, 10 words, 1 OOVs
0 zeroprobs, logprob= -9.888721 ppl= 6.66899 ppl1= 12.55298
```

# Lời cảm ơn

Hướng dẫn sử dụng được tham khảo từ các nguồn 

* [Install SRILM on Ubuntu](https://hoxuanvinh.wordpress.com/2016/04/22/install-srilm-on-ubuntu/)
* http://idiom.ucsd.edu/~rlevy/teaching/2015winter/lign165/lectures/lecture13/lecture13_ngrams_with_SRILM.pdf

