from utils import itsOption
from loans.admin_room_loans_functions import (
    load_users,
    load_room_loans,
    print_loans,
    search_loans_by_room_name,
    search_loans_by_user_name,
    view_user_loans_admin,
)


def admin_room_loans_menu():

    loans = load_room_loans()
    users = load_users()

    users_dict = {u["id"]: u for u in users}

    while True:
        print("\n-*--*-View room loans [admin]-*--*-")
        print("1. List all loans")
        print("2. Search Loans")
        print("3. Go back")
        print("-*--*-*--*-*--*-*--*-*--*-*--*\n")

        option = input("> ").strip()

        if not itsOption(option, ["1", "2", "3"]):
            print("Invalid option.")
            continue

        if option == "1":
            print_loans(loans, users_dict)
        elif option == "2":
            search_loans_menu(loans, users_dict)
        elif option == "3":
            break



def search_loans_menu(loans, users_dict):
    while True:
        print("\n-*--*-Search room loans [admin]-*--*-")
        print("1. Search by user id")
        print("2. Search by user name")
        print("3. Search by room name")
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
            view_user_loans_admin(int(user_id), loans, users_dict)

        elif option == "2":
            user_name = input("User name: \n").strip()
            search_loans_by_user_name(user_name, loans, users_dict)

        elif option == "3":
            room_name = input("Room name: \n").strip()
            search_loans_by_room_name(room_name, loans, users_dict)

        elif option == "4":
            break
