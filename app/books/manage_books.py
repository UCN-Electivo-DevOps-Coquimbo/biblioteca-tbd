import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "book.json")

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

def edit_book():
    books = get_books()
    if not books:
        print("\nNo books registered.")
        return

    list_books()
    book_id = input("\nEnter the ID of the book to edit: ").strip()

    if not book_id.isdigit():
        print("Invalid ID.")
        return

    book = None
    for b in books:
        if b["id"] == int(book_id):
            book = b
            break
    if not book:
        print(f"No book found with ID {book_id}.")
        return

    print(f"\nEditing book: [{book['id']}] {book['title']}")
    print("(Press Enter to keep the current value)")

    title = input(f"Title [{book['title']}]: ").strip()
    author = input(f"Author [{book['author']}]: ").strip()
    editorial = input(f"Editorial [{book['editorial']}]: ").strip()
    year = input(f"Year [{book['year']}]: ").strip()
    genre = input(f"Genre [{book['genre']}]: ").strip()
    total_copies = input(f"Total Copies [{book['total_copies']}]: ").strip()

    if title:
        book["title"] = title
    if author:
        book["author"] = author
    if editorial:
        book["editorial"] = editorial
    if year:
        if not year.isdigit():
            print("Invalid year. Changes to year were not saved.")
        else:
            book["year"] = int(year)
    if genre:
        book["genre"] = genre
    if total_copies:
        if not total_copies.isdigit():
            print("Invalid number. Changes to total copies were not saved.")
        else:
            new_total = int(total_copies)
            copies_in_use = book["total_copies"] - book["available_copies"]
            new_available = new_total - copies_in_use
            if new_available < 0:
                print(f"Cannot reduce total copies to {new_total}. There are {copies_in_use} copies currently on loan.")
            else:
                book["total_copies"] = new_total
                book["available_copies"] = new_available

    save_books(books)
    print(f"\nBook '{book['title']}' updated successfully.")

def manage_books():
    while True:
        print("\nManage Books")
        print("1. View all books")
        print("2. Add book")
        print("3. Edit book")
        print("4. Go back")
        opcion = input("> ").strip()

        if opcion == "1":
            list_books()
        elif opcion == "2":
            create_book()
        elif opcion == "3":
            edit_book()
        elif opcion == "4":
            break
        else:
            print("Invalid option.")
