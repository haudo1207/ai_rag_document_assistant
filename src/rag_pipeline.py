import json
import time
from pathlib import Path
from ask_llm import ask_llm

BASE_DIR = Path(__file__).resolve().parent.parent


def load_chunks(path: str):
    file_path = BASE_DIR / path

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def simple_retrieve(question: str, chunks, top_k: int = 3):
    question_words = question.lower().split()
    scored_chunks = []

    for chunk in chunks:
        content = chunk["content"].lower()
        score = 0

        for word in question_words:
            if word in content:
                score += 1

        scored_chunks.append({
            "chunk_id": chunk["chunk_id"],
            "content": chunk["content"],
            "score": score
        })

    scored_chunks = sorted(
        scored_chunks,
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_chunks[:top_k]


def build_prompt(question: str, retrieved_chunks):
    context = "\n\n".join([
        f"[{chunk['chunk_id']}]\n{chunk['content']}"
        for chunk in retrieved_chunks
    ])

    prompt = f"""
Bạn là trợ lý AI trả lời câu hỏi dựa trên tài liệu.

Nguyên tắc:
1. Chỉ sử dụng thông tin trong CONTEXT.
2. Không tự bịa thông tin.
3. Nếu CONTEXT không có thông tin, hãy trả lời: "Tôi chưa tìm thấy thông tin này trong tài liệu."
4. Trả lời bằng tiếng Việt, ngắn gọn, rõ ràng.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    return prompt


def answer_question(question: str):
    start_time = time.time()

    chunks = load_chunks("data/chunks.json")

    retrieved_chunks = simple_retrieve(
        question=question,
        chunks=chunks,
        top_k=3
    )

    prompt = build_prompt(question, retrieved_chunks)

    answer = ask_llm(prompt)

    latency = time.time() - start_time

    return {
        "question": question,
        "retrieved_chunks": retrieved_chunks,
        "answer": answer,
        "latency": latency
    }


if __name__ == "__main__":
    question = input("Nhập câu hỏi về tài liệu: ")

    result = answer_question(question)

    print("\nCác chunk được retrieve:")
    for chunk in result["retrieved_chunks"]:
        print(f"- {chunk['chunk_id']} | score={chunk['score']}")

    print("\nAI trả lời:")
    print(result["answer"])

    print(f"\nTổng thời gian: {result['latency']:.2f} giây")