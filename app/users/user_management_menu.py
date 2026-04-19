from users.user_actions import (
    create_user, 
    delete_user, 
    edit_user_menu, 
    find_user, 
    list_all_users
)

def user_management_menu(current_user_role):
    while True:
        print("\n" + "="*25)
        print("   USER MANAGEMENT")
        print("="*25)
        print("1. Create user")
        print("2. Search user")
        print("3. List all users")
        print("4. Edit user")
        print("5. Delete user")
        print("6. Back")

        option = input("> ").strip()

        if option == "1":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role (admin/student): ")
            create_user(current_user_role, name, email, password, role)

        elif option == "2":
            find_user()

        elif option == "3":
            list_all_users()

        elif option == "4":
            target = input("Enter the name of the user to edit: ")
            edit_user_menu(target, current_user_role)

        elif option == "5":
            target = input("Enter the name of the user to delete: ")
            delete_user(current_user_role, target)

        elif option == "6":
            print("Returning to main menu...")
            break
        else:
            print("Invalid option, please try again.")