from auth import login, register
import menu.index as menu_index
import utils as biblioteca_utils

def main():
    option = ""
    while(not biblioteca_utils.itsOption(option, ["1", "2", "3"], int)):
        print("=== Library UCN ===")
        print("1) Log in")      
        print("2) Register")
        print("3) Exit")
        option = input("> ")

    if(option == "1"):
        user = login()
        if user:
            print(f"\n[Active account: {user['email']}]")
            if user["rol"] == "student":
                menu_index.menu(user["id"], "student") # aqui se llama al menu del alumno, pero se puede cambiar a admin dependiendo del tipo de usuario
            else:
                menu_index.menu(user["id"], "admin")
    elif(option == "2"):
        register()
    elif option == "3":
        print("See you soon.")
    else:
        print("invalid option")



if __name__ == "__main__":
    main()


