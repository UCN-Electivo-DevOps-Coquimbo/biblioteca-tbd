from app.study_rooms import reserve_study_room, add_study_room, delete_study_room, edit_study_room

def show_menu():
    print("------MENU ADMINISTRADOR SALAS DE ESTUDIO-------")
    print("Ingresa el número de la opción que deseas realizar:")
    print("1. Reservar sala de estudio")
    print("2. Agregar sala de estudio")
    print("3. Editar sala de estudio")
    print("4. Eliminar sala de estudio")
    while True:
        option = input("Opción: ")
        if option == "1":
            reserve_study_room()
        elif option == "2":
            add_study_room()
        elif option == "3":
            edit_study_room()
        elif option == "4":
            delete_study_room()
        elif option == "0":
            print("Saliendo del menú de salas de estudio.")
            break

if __name__ == "__main__":
    show_menu()