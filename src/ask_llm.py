import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Thiếu GEMINI_API_KEY trong file .env")

client = genai.Client(api_key=API_KEY)


def ask_llm(question: str) -> str:
    start_time = time.time()

    prompt = f"""
Bạn là trợ lý AI hữu ích.
Hãy trả lời bằng tiếng Việt, ngắn gọn, dễ hiểu.

Câu hỏi:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        response_text = response.text

    except Exception as e:
        response_text = f"Lỗi khi gọi Gemini API: {e}"

    latency = time.time() - start_time
    print(f"Thời gian phản hồi: {latency:.2f} giây")

    return response_text


if __name__ == "__main__":
    question = input("Nhập câu hỏi: ")
    answer = ask_llm(question)

    print("\nAI trả lời:")
    print(answer)