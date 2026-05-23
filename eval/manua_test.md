# Manual Test
## Test1

Nhập câu hỏi về tài liệu: Chương trình AI Level 1 tập trung vào những gì?
Thời gian phản hồi: 2.06 giây

AI trả lời:
Chương trình AI Level 1 tập trung vào Python, Prompt Engineering, Gemini API, RAG cơ bản và đánh giá mô hình.

Result: Đúng.

## Test2

Nhập câu hỏi về tài liệu: Ứng viên cần hoàn thành POC gì?
Thời gian phản hồi: 1.92 giây

Các chunk được retrieve:
- chunk_1 | score=6
- chunk_2 | score=3
- chunk_3 | score=2

AI trả lời:
Ứng viên cần hoàn thành một mini POC về hỏi đáp tài liệu bằng RAG. POC này cần có source code, README, eval set và report.

Result: Đúng.

## Test3
Nhập câu hỏi về tài liệu: Tiêu chí đánh giá gồm những gì?
Thời gian phản hồi: 1.52 giây

Các chunk được retrieve:
- chunk_1 | score=5
- chunk_2 | score=5
- chunk_3 | score=2

AI trả lời:
Tiêu chí đánh giá gồm accuracy, hallucination rate, latency và cost per query.

Result: Đúng.

## Test4
Nhập câu hỏi về tài liệu: Demo nên kéo dài bao lâu?        
Thời gian phản hồi: 2.46 giây

Các chunk được retrieve:
- chunk_2 | score=2
- chunk_1 | score=0
- chunk_3 | score=0

AI trả lời:
Demo nên kéo dài 2-4 phút.

Result: Đúng.

## Test5
Nhập câu hỏi về tài liệu: Lương của vị trí này là bao nhiêu?
Thời gian phản hồi: 2.39 giây

Các chunk được retrieve:
- chunk_1 | score=0
- chunk_2 | score=0
- chunk_3 | score=0

AI trả lời:
Tôi chưa tìm thấy thông tin này trong tài liệu.

Result: Đúng vì không hallucinate.