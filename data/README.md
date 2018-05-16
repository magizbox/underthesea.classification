# Mô tả định dạng dữ liệu cho corpus cho bài toán phân loại văn bản

Phiên bản 1.0.0 - 20180516

Corpus được lưu dưới dạng một thư mục, chứa nhiều thư mục con. Ví dụ tập huấn luyện trong dữ liệu VNTC được lưu trong thư mục `VNTC/corpus/train`, chứa 13 thư mục con `Chinh tri`, `Xa hoi`, `Doi song`, `Khoa hoc`, `Kinh doanh`, `Phap luat`, `Suc khoe`, `The gioi`, `The thao`,  `Van hoa`, `Vi tinh`.

Mỗi thư mục con chứa các bài viết tương ứng trong chủ đề, mỗi bài viết được lưu vào một file. Ví dụ, mục `Chinh tri` trong dữ liệu huấn luyên của tập VNTC được lưu trong thư mục `VNTC/corpus/train/Chinh tri`, gồm 5222 file

```
XH_NLD_ (3672).txt  XH_NLD_ (4107).txt  XH_NLD_ (4542).txt  XH_NLD_ (4977).txt 
XH_TN_ (1364).txt  XH_TN_ (1799).txt  XH_TT_ (2387).txt  XH_TT_ (2822).txt 
XH_TT_ (3257).txt   XH_VNE_ (1019).txt  XH_VNE_ (218).txt  XH_VNE_ (60).txt
XH_NLD_ (3673).txt  XH_NLD_ (4108).txt  XH_NLD_ (4543).txt  XH_NLD_ (4978).txt 
XH_TN_ (1365).txt  XH_TN_ (1800).txt  XH_TT_ (2388).txt  XH_TT_ (2823).txt 
XH_TT_ (3258).txt   XH_VNE_ (101).txt   XH_VNE_ (219).txt  XH_VNE_ (610).txt
...
```
 