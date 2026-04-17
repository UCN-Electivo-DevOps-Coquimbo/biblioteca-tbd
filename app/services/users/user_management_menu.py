from create_user import crear_usuario
from delete_user import eliminar_usuario
from edit_user import editar_usuario
from get_user import get_usuario
from get_users import obtener_usuarios

def user_management_menu():
    opcion = ""
    while True:
        print("\n=== Gestionar Usuarios ===")
        print("1. Crear usuario")
        print("2. Buscar usuario")
        print("3. Listar usuarios")
        print("4. Editar usuario")
        print("5. Eliminar usuario")
        print("6. Volver")

        opcion = input("> ").strip()

        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            get_usuario()
        elif opcion == "3":
            obtener_usuarios()
        elif opcion == "4":
            editar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente nuevamente.")