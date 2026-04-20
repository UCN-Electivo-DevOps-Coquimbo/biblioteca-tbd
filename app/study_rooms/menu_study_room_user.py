from app.study_rooms import reserve_study_room_user, cancel_study_room_user

def show_menu(user_id):
    while True:
        print("------STUDY ROOM USER MENU-------")
        print("Enter the number of the option you want to perform:")
        print("1. Reserve study room")
        print("2. Cancel study room")
        option = input("Option: ")
        if option == "1":
            reserve_study_room_user(user_id)
        elif option == "2":
            cancel_study_room_user(user_id)
        elif option == "0":
            print("Exiting study room menu.")
            break

if __name__ == "__main__":
    show_menu(None)
