import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "libros.json")

def get_books():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def create_book():
    print("\nCreate Book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    editorial = input("Editorial: ").strip()
    year = input("Year: ").strip()
    genre = input("Genre: ").strip()
    total_copies = input("Total Copies: ").strip()

    books = get_books()
    new_id = max((b["id"] for b in books), default=0) + 1

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "editorial": editorial,
        "year": int(year),
        "genre": genre,
        "total_copies": int(total_copies),
        "available_copies": int(total_copies)
    }

    books.append(new_book)
    save_books(books)
    print(f"\nThe book '{title}' was added successfully.")

def list_books():
    books = get_books()
    if not books:
        print("\nNo books registered.")
        return
    print("\nAvailable books")
    for b in books:
        print(f"[{b['id']}] Title: {b['title']}, Author: {b['author']}, Editorial: {b['editorial']}, Year: {b['year']}, Genre: {b['genre']}, Total Copies: {b['total_copies']}, Available Copies: {b['available_copies']}")

def manage_books():
    while True:
        print("\nManage Books")
        print("1. View all books")
        print("2. Add book")
        print("3. Go back")
        opcion = input("> ").strip()

        if opcion == "1":
            list_books()
        elif opcion == "2":
            create_book()
        elif opcion == "3":
            break
        else:
            print("Invalid option.")
