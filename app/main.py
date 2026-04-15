import menu.index as menu_index
import utils as biblioteca_utils

def main():
    print("Base biblioteca UCN")
    opcion = ""
    while(not biblioteca_utils.esOpcion(opcion, ["1", "2"], int)):

        print("1) Iniciar sesion")      
        print("2) Registrarse")
        opcion = input("> ")

    if(opcion == "1"):
        print("Iniciar sesion")
        # aqui iria el codigo para iniciar sesion, pero por ahora solo es un mensaje

        menu_index.menu("alumno") # aqui se llama al menu del alumno, pero se puede cambiar a admin dependiendo del tipo de usuario


    elif(opcion == "2"):
        print("Registrarse")
        # aqui iria el codigo para registrarse, pero por ahora solo es un mensaje




if __name__ == "__main__":
    main()


