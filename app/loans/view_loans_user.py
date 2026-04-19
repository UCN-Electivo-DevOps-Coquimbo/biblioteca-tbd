import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH_LOANS = os.path.join(BASE_DIR, "data", "loans.json")
DATA_PATH_BOOKS = os.path.join(BASE_DIR, "data", "book.json")

def load_json_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def view_my_loans(user_id):
    loans = load_json_data(DATA_PATH_LOANS)
    books = load_json_data(DATA_PATH_BOOKS)

    books_dict = {b["id"]: b for b in books}
    
    if not loans:
        print("No hay préstamos registrados.")
        return

    print("\n" + "="*50)
    print("       HISTÓRICO DE PRÉSTAMOS DETALLADO")
    print("="*50)

    has_loans = False

    for loan in loans:
        if (loan["user_id"] == user_id):
            has_loans = True
            book = books_dict.get(loan["book_id"])

            book_title = book["title"] if book else "Libro no encontrado"
            book_author = book["author"] if book else "N/A"
            
            print(f"ID Préstamo: {loan['id']}")
            print(f"Libro:    {book_title} ({book_author})")
            print(f"Fecha préstamo: {loan['loan_date']}")
            print(f"Fecha devolución: {loan['return_date']}")
            print("-" * 50)
    
    if (not has_loans):
        print("Sin préstamos realizados.\n")
    