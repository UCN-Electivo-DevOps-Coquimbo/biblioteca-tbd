from auth import login, register
import menu.index as menu_index
import utils as biblioteca_utils

def main():
    print("Base biblioteca UCN")
    opcion = ""
    while(not biblioteca_utils.esOpcion(opcion, ["1", "2"], int)):
        print("=== Biblioteca UCN ===")
        print("1) Iniciar sesion")      
        print("2) Registrarse")
        print("3) Salir")
        opcion = input("> ")

    if(opcion == "1"):
        usuario = login()
        if usuario:
            print(f"\n[Sesión activa como: {usuario['email']}]")
            if usuario["rol"] == "estudiante":
                menu_index.menu("alumno") # aqui se llama al menu del alumno, pero se puede cambiar a admin dependiendo del tipo de usuario
    elif(opcion == "2"):
        register()
    elif opcion == "3":
        print("Hasta luego.")
    else:
        print("Opción inválida.")



if __name__ == "__main__":
    main()


