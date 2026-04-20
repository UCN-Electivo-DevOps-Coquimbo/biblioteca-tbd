from study_rooms import menu_study_room_user
from books.manage_books import manage_books
from loans.view_loans_user import view_my_loans
from loans.admin_book_loans_menus import admin_book_loans_menu
from books.borrow_menu import borrow_return_menu
from services.debt import debt_menu

student_options = ["1", "2", "3", "4", "5"]
admin_options = ["1", "2", "3", "4", "5"]
def menu(user_id, userType = "student"):
    option = ""
    if(userType == "student"):
        options = student_options
    else:
        options = admin_options

    while(True):
        printMenu(userType)
        option = input("> ")
        if(userType == "student"):
            if(option == "1"):
                borrow_return_menu(user_id)

            elif(option == "2"):
                print("Request a study room")
                menu_study_room_user.show_menu(user_id)

            elif(option == "3"):
                view_my_loans(user_id)
            elif(option == "4"):
                print("Debt section")
                debt_menu(user_id)
            elif(option == "5"):
                print("Exit")
                break
            else:
                print("Invalid option, please enter a valid option")
        else:
            if(option == "1"):
                manage_books()
            elif(option == "2"):
                print("request as study room")
                # aqui iria el codigo para gestionar las salas de estudio, pero por ahora solo es un mensaje
            elif(option == "3"):
                print("View Loans")
                # aqui iria el codigo para visualizar los prestamos, pero por ahora solo es un mensaje
                admin_book_loans_menu()
            elif(option == "4"):
                print("Manage Users")
                # aqui iria el codigo para gestionar los usuarios, pero por ahora solo es un mensaje
            elif(option == "5"):
                print("Exit")
                break
            else:
                print("Invalid option, please enter a valid option")
    


def printMenu(userType = "student"):
    print("Welcome to the library")
    if(userType == "student"):
        print("1. Borrow book")
        print("2. Request study room")
        print("3. View loans")
        print("4. Debt section")

    else:
        print("1. Manage Books")
        print("2. Manage Study Rooms")
        print("3. View Loans")
        print("4. Manage Users")
    

    print("5. Exit")
