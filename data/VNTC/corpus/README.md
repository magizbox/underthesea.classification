# Text Classification format

Corpus is stored in excel (.xlsx) file. Which has one `text` column, each label has a corresponding column.

Example

| text                                                                       | Xã hội | Giáo dục | Thể thao |
|----------------------------------------------------------------------------|--------|----------|----------|
| Xe sang 6 tỷ tông vỡ nát xe máy, tài xế đi khỏi hiện trường                | 1      | 0        | 0        |
| Phát hiện thẩm phán TAND thành phố Thái Nguyên dùng bằng giả               | 1      | 0        | 0        |
| TPHCM xây trung tâm hành chính 18.000 m2 trên “đất vàng”                   | 1      | 0        | 0        |
| Xúc động hình ảnh cô giáo vùng cao gồng mình cõng bàn ghế cho học trò      | 0      | 1        | 0        |
| TPHCM: Giáo viên mầm non có trình độ Thạc sĩ được hỗ trợ 18 triệu đồng/năm | 0      | 1        | 0        |
| Cô giáo lao vào đám cháy “cứu” giấy tờ, tài sản… bị bỏng nặng              | 0      | 1        | 0        |
| Chơi xấu đối thủ, Marcelo có nguy cơ bị treo giò 4 trận                    | 0      | 0        | 1        |
| Cổ động viên Thanh Hoá nhuộm vàng sân Thông Nhất                           | 0      | 0        | 1        |
| 5 golf thủ Việt sẽ tham gia vòng chung kết WAGC 2017 tại Malaysia          | 0      | 0        | 1        |