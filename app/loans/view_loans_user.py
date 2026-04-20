import utils as biblioteca_utils
from utils import DATA_PATH_LOANS, DATA_PATH_BOOKS


def view_my_loans(user_id):
    loans_data = biblioteca_utils.load_json_data(DATA_PATH_LOANS)
    loans = loans_data.get("loans", []) if isinstance(loans_data, dict) else loans_data
    books = biblioteca_utils.load_json_data(DATA_PATH_BOOKS)

    books_dict = {b["id"]: b for b in books}
    
    if not loans:
        print("No loan records found.")
        return

    print("\n" + "="*50)
    print("       'DETAILED LOAN HISTORY'")
    print("="*50)

    has_loans = False

    for loan in loans:
        if (loan["user_id"] == user_id):
            has_loans = True
            book = books_dict.get(loan["book_id"])

            book_title = book["title"] if book else "Book not found"
            book_author = book["author"] if book else "N/A"
            
            print(f"Loan ID: {loan['id']}")
            print(f"Book:    {book_title} ({book_author})")
            print(f"Loan Date: {loan['loan_date']}")
            print(f"Return Date: {loan['return_date']}")
            print("-" * 50)
    
    if (not has_loans):
        print("No loans recorded for this user.\n")
    