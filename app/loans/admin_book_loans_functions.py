import utils as biblioteca_utils
from utils import DATA_PATH_USERS, DATA_PATH_LOANS


def load_users():
    users_data = biblioteca_utils.load_json_data(DATA_PATH_USERS)
    if isinstance(users_data, dict):
        return users_data.get("users", [])
    return []


def load_loans():
    loans_data = biblioteca_utils.load_json_data(DATA_PATH_LOANS)
    if isinstance(loans_data, dict):
        return loans_data.get("loans", [])
    return []


def get_column_widths(loans, users_dict, books_dict):
    widths = {
        'loan_id': len('Loan ID'),
        'user_id': len('User ID'),
        'user': len('User'),
        'book': len('Book'),
        'loan_date': len('Loan Date'),
        'return_date': len('Return Date')
    }
    
    for loan in loans:
        widths['loan_id'] = max(widths['loan_id'], len(str(loan['id'])))
        widths['user_id'] = max(widths['user_id'], len(str(loan['user_id'])))
        
        user = users_dict.get(loan['user_id'])
        user_name = user['name'] if user else 'User not found'
        widths['user'] = max(widths['user'], len(user_name))
        
        book = books_dict.get(loan['book_id'])
        book_title = book['title'] if book else 'Book not found'
        widths['book'] = max(widths['book'], len(book_title))
        
        widths['loan_date'] = max(widths['loan_date'], len(loan['loan_date']))
        widths['return_date'] = max(widths['return_date'], len(loan['return_date']))
    
    return widths


def view_user_loans_admin(user_id, loans, books_dict):
    if not loans:
        print("No loans found.")
        return

    has_loans = False
    for loan in loans:
        if loan["user_id"] == user_id:
            has_loans = True
            book = books_dict.get(loan["book_id"])

            book_title = book["title"] if book else "Book not found"
            book_author = book["author"] if book else "N/A"

            print(f"Loan ID: {loan['id']}")
            print(f"Book:    {book_title} ({book_author})")
            print(f"Loan Date: {loan['loan_date']}")
            print(f"Return Date: {loan['return_date']}")
            print("-" * 50)

    if not has_loans:
        print("This user doesn't have loans.\n")


def print_loans(loans, users_dict, books_dict):
    if not loans:
        print("No loans found.")
        return

    widths = get_column_widths(loans, users_dict, books_dict)
    
    header = f"{'Loan ID':<{widths['loan_id']}} | {'User ID':<{widths['user_id']}} | {'User':<{widths['user']}} | {'Book':<{widths['book']}} | {'Loan Date':<{widths['loan_date']}} | {'Return Date':<{widths['return_date']}}"
    separator = "-" * len(header)
    
    print("\n" + "=" * len(header))
    print(header)
    print(separator)

    for loan in loans:
        user = users_dict.get(loan["user_id"])
        book = books_dict.get(loan["book_id"])

        user_name = user["name"] if user else "User not found"
        book_title = book["title"] if book else "Book not found"

        print(f"{loan['id']:<{widths['loan_id']}} | {loan['user_id']:<{widths['user_id']}} | {user_name:<{widths['user']}} | {book_title:<{widths['book']}} | {loan['loan_date']:<{widths['loan_date']}} | {loan['return_date']:<{widths['return_date']}}")

    print(separator)


def search_loans_by_user_name(user_name, loans, books_dict, users_dict):
    user_name = user_name.strip().lower()
    
    matching_user_ids = []
    for user_id, user in users_dict.items():
        if user_name in user["name"].lower():
            matching_user_ids.append(user_id)
    
    if not matching_user_ids:
        print("No users found with that name.")
        return
    
    result = [loan for loan in loans if loan["user_id"] in matching_user_ids]
    print_loans(result, users_dict, books_dict)


def search_loans_by_book_name(book_name, loans, books_dict, users_dict):
    book_name = book_name.strip().lower()

    matching_book_ids = []
    for book_id, book in books_dict.items():
        if book_name in book["title"].strip().lower():
            matching_book_ids.append(book_id)

    if not matching_book_ids:
        print("No books found with that name.")
        return

    result = [loan for loan in loans if loan["book_id"] in matching_book_ids]
    print_loans(result, users_dict, books_dict)
