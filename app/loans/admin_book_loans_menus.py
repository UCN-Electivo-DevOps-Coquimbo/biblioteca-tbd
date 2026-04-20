import utils as biblioteca_utils
from utils import itsOption, DATA_PATH_LOANS, DATA_PATH_BOOKS
from loans.admin_book_loans_functions import (
    get_user_id_by_name,
    load_users,
    load_loans,
    print_loans,
    search_loans_by_book_name,
    search_loans_by_user_name,
    view_user_loans_admin,
)


def admin_book_loans_menu():

    loans = load_loans()
    books = biblioteca_utils.load_json_data(DATA_PATH_BOOKS)
    users = load_users()

    users_dict = {u["id"]: u for u in users} 
    books_dict = {b["id"]: b for b in books}

    while True:
        print("\n-*--*-View loans [admin]-*--*-")
        print("1. List all loans")
        print("2. Search Loans")
        print("3. Go back")
        print("-*--*-*--*-*--*-*--*-*--*-*--*\n")

        option = input("> ").strip()

        if not itsOption(option, ["1", "2", "3"]):
            print("Invalid option.")
            continue

        if option == "1":
            print_loans(loans, users_dict, books_dict)
        elif option == "2":
            search_loans_menu(loans, books_dict, users_dict)
        elif option == "3":
            break



def search_loans_menu(loans, books_dict, users_dict):
    while True:
        print("\n-*--*-Search book loans [admin]-*--*-")
        print("1. Search by user id")
        print("2. Search by user name")
        print("3. Search by book name")
        print("4. Go back")
        print("-*--*-*--*-*--*-*--*-*--*--*-*--*-*--\n")

        option = input("> ").strip()

        if not itsOption(option, ["1", "2", "3", "4"]):
            print("Invalid option.")
            continue

        if option == "1":
            user_id = input("User id: \n").strip()
            if not user_id.isdigit():
                print("Invalid id.")
                continue
            view_user_loans_admin(int(user_id), loans, books_dict)

        elif option == "2":
            user_name = input("User name: \n").strip()
            search_loans_by_user_name(user_name, loans, books_dict, users_dict)

        elif option == "3":
            book_name = input("Book name: \n").strip()
            search_loans_by_book_name(book_name, loans, books_dict, users_dict)

        elif option == "4":
            break
