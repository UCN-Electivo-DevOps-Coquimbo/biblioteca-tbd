def borrow_return_menu():
    from books.book_actions import borrow_book, return_book

    while True:
        print("\n=== Borrow / Return Menu ===")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Back")

        option = input("Choose an option: ").strip()

        if option == "1":
            borrow_book()
        elif option == "2":
            return_book()
        elif option == "3":
            break
        else:
            print("Invalid option. Try again.")