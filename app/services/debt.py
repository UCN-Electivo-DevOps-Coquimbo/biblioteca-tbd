import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH_LOANS = os.path.join(BASE_DIR, "data", "loans.json")
DATA_PATH_BOOKS = os.path.join(BASE_DIR, "data", "book.json")


def load_loans():
    with open(DATA_PATH_LOANS, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        loans = data.get("loans", [])
        return loans if isinstance(loans, list) else []

    if isinstance(data, list):
        return data

    return []


def save_loans(loans):
    data_to_save = loans
    if os.path.exists(DATA_PATH_LOANS):
        with open(DATA_PATH_LOANS, "r", encoding="utf-8") as f:
            current_data = json.load(f)
        if isinstance(current_data, dict):
            current_data["loans"] = loans
            data_to_save = current_data

    with open(DATA_PATH_LOANS, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=2)


def load_books():
    with open(DATA_PATH_BOOKS, "r", encoding="utf-8") as f:
        return json.load(f)


def debt_menu(user_id):
    while True:
        print("\n=== Debt Section ===")
        print("What do you want to do:")
        print("1. View debt")
        print("2. Pay off debts")
        print("3. Return to main menu")
        opcion = input("> ")
        if opcion == "1":
            view_debt(user_id)
        elif opcion == "2":
            pay_off_debts(user_id)
        elif opcion == "3":
            break
        else:
            print("Invalid option, please select a valid number.")


def view_debt(user_id):
    loans = load_loans()
    books = load_books()
    books_dict = {book["id"]: book for book in books}
    user_loans = [loan for loan in loans if loan.get("user_id") == user_id]

    print("\nView debt")

    if not user_loans:
        print("No loans found for this user.")
        return

    for loan in user_loans:
        debt_status = loan.get("debt", False)
        book = books_dict.get(loan.get("book_id"))
        book_title = book["title"] if book else "Book not found"
        book_author = book["author"] if book else "N/A"

        print(f"Loan ID: {loan.get('id')}")
        print(f"Book: {book_title} ({book_author})")
        print(f"Debt: {'Yes' if debt_status else 'No'}")
        print("-" * 30)


def pay_off_debts(user_id):
    loans = load_loans()
    user_debts = [loan for loan in loans if loan.get("user_id") == user_id and loan.get("debt", False)]

    print("\nPay off debts")

    if not user_debts:
        print("No debts found for this user.")
        return

    print("Loans with debt:")
    for loan in user_debts:
        print(f"Loan ID: {loan.get('id')}")

    loan_id = input("Enter the Loan ID to pay: ").strip()
    if not loan_id.isdigit():
        print("Invalid Loan ID.")
        return

    loan_id = int(loan_id)
    loan_to_pay = None
    for loan in loans:
        if loan.get("user_id") == user_id and loan.get("id") == loan_id and loan.get("debt", False):
            loan_to_pay = loan
            break

    if not loan_to_pay:
        print("No debt found with that Loan ID.")
        return

    loan_to_pay["debt"] = False
    save_loans(loans)
    print(f"Loan {loan_id} debt paid successfully.")

