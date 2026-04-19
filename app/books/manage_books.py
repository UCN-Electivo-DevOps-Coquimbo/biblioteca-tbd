from books.book_actions import create_book, list_books, edit_book, delete_book

def manage_books():
    while True:
        print("\nManage Books")
        print("1. View all books")
        print("2. Add book")
        print("3. Edit book")
        print("4. Delete book")
        print("5. Go back")
        opcion = input("> ").strip()

        if opcion == "1":
            list_books()
        elif opcion == "2":
            create_book()
        elif opcion == "3":
            edit_book()
        elif opcion == "4":
            delete_book()
        elif opcion == "5":
            break
        else:
            print("Invalid option.")
