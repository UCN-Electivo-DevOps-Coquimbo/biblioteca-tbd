from study_rooms import reserve_study_room, add_study_room, delete_study_room, edit_study_room

def show_menu():
    print("------STUDY ROOM ADMIN MENU-------")
    print("Enter the number of the option you want to perform:")
    print("1. Reserve study room")
    print("2. Add study room")
    print("3. Edit study room")
    print("4. Delete study room")
    while True:
        option = input("Option: ")
        if option == "1":
            reserve_study_room()
        elif option == "2":
            add_study_room()
        elif option == "3":
            edit_study_room()
        elif option == "4":
            delete_study_room()
        elif option == "0":
            print("Exiting study room menu.")
            break

if __name__ == "__main__":
    show_menu()