import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "book.json")

def get_books():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
