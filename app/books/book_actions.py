import json
from datetime import date, timedelta

from books.book_repository import get_books, save_books
from utils import DATA_PATH_LOANS


def _load_loans_data():
    with open(DATA_PATH_LOANS, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        loans = data.get("loans", [])
        if not isinstance(loans, list):
            data["loans"] = []
            loans = data["loans"]
        return data, loans

    if isinstance(data, list):
        return data, data

    return {"loans": []}, []


def _save_loans_data(data):
    with open(DATA_PATH_LOANS, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _register_loan(book_id, user_id):
    data, loans = _load_loans_data()
    next_id = max((loan.get("id", 0) for loan in loans if isinstance(loan, dict)), default=0) + 1

    loan_date = date.today()
    return_date = loan_date + timedelta(days=14)

    new_loan = {
        "id": next_id,
        "book_id": book_id,
        "user_id": user_id,
        "loan_date": loan_date.strftime("%d-%m-%Y"),
        "return_date": return_date.strftime("%d-%m-%Y"),
        "debt": False,
    }

    loans.append(new_loan)
    _save_loans_data(data)


def _remove_loan_on_return(book_id, user_id):
    data, loans = _load_loans_data()

    for i in range(len(loans) - 1, -1, -1):
        loan = loans[i]
        if not isinstance(loan, dict):
            continue
        if loan.get("book_id") != book_id:
            continue
        if loan.get("user_id") != user_id:
            continue

        loans.pop(i)
        _save_loans_data(data)
        return True

    return False

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

def delete_book():
    books = get_books()
    if not books:
        print("\nNo books registered.")
        return

    list_books()
    book_id = input("\nEnter the ID of the book to delete: ").strip()

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

    print(f"\nBook to delete: [{book['id']}] {book['title']} - {book['author']}")

    copies_in_use = book["total_copies"] - book["available_copies"]
    if copies_in_use > 0:
        print(f"Cannot delete: this book has {copies_in_use} copy(ies) currently on loan.")
        return

    confirm = input("Are you sure you want to delete this book and all its copies? (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return

    books = [b for b in books if b["id"] != int(book_id)]
    save_books(books)
    print(f"\nBook '{book['title']}' deleted successfully.")

def borrow_book(user_id=None):
    books = get_books()
    if not books:
        print("\nNo books registered.")
        return

    list_books()
    book_id = input("\nEnter the ID of the book to borrow: ").strip()

    if not book_id.isdigit():
        print("Invalid ID.")
        return

    for book in books:
        if book["id"] == int(book_id):
            if book["available_copies"] > 0:
                book["available_copies"] -= 1
                save_books(books)
                if user_id is not None:
                    _register_loan(book["id"], user_id)
                print(f"\nYou borrowed '{book['title']}' successfully.")
            else:
                print("\nNo copies available for this book.")
            return

    print("Book not found.")

def return_book(user_id=None):
    books = get_books()
    if not books:
        print("\nNo books registered.")
        return

    list_books()
    book_id = input("\nEnter the ID of the book to return: ").strip()

    if not book_id.isdigit():
        print("Invalid ID.")
        return

    for book in books:
        if book["id"] == int(book_id):
            if book["available_copies"] < book["total_copies"]:
                book["available_copies"] += 1
                save_books(books)
                if user_id is not None:
                    _remove_loan_on_return(book["id"], user_id)
                print(f"\nYou returned '{book['title']}' successfully.")
            else:
                print("\nAll copies are already in the library.")
            return

    print("Book not found.")
