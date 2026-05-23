import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_text(file_path: str) -> str:
    path = BASE_DIR / file_path

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def split_text(text: str, chunk_size: int = 300, overlap: int = 50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk_content = text[start:end]

        chunks.append({
            "chunk_id": f"chunk_{len(chunks) + 1}",
            "content": chunk_content
        })

        start = end - overlap

    return chunks


def save_chunks(chunks, output_path: str):
    path = BASE_DIR / output_path

    with open(path, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    text = load_text("data/sample_document.txt")
    chunks = split_text(text, chunk_size=300, overlap=75)
    save_chunks(chunks, "data/chunks.json")

    print(f"Đã tạo {len(chunks)} chunks.")
    print("File output: data/chunks.json")