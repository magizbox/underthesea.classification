# Underthesea Text Classification Data Format

```
Author  : Vu Anh
Version : 1.0
Date    : 2018/08/15 
```

Files are encoded in plain text files (UTF-8, using only LF characters as line break, including an LF character at the end of file)

Each line of text file contains a label, followed by the corresponding document. All the labels start by `__label__` prefix, which is how system recognize what is a label or what is a word.

Example 

```
__label__giao_duc Bất ngờ tranh luận quanh bìa SGK Lịch sử lớp 7 có hình Vạn Lý Trường Thành
__label__giao_duc Tuyển sinh lớp 10 năm 2019 của Hà Nội: Chọn phương án nào hữu hiệu?
__label__giao_duc Hơn 122.000 giáo viên mầm non nghỉ công tác chưa được hưởng chế độ
__label__the_thao Báo chí Đông Nam Á hết mực khen ngợi Olympic Việt Nam
__label__the_thao “Không nên để Công Phượng tiếp tục đá phạt đền!”
__label__the_thao Chia tay Tottenham, ngôi sao Son Heung-min về thi đấu ở Asiad 2018
```

