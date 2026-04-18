from services.get_book import solicitar_prestamo_libro
from services.manage_books import manage_books

student_options = ["1", "2", "3", "4", "5"]
admin_options = ["1", "2", "3", "4", "5"]
def menu(userType = "student"):
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
                solicitar_prestamo_libro()

            elif(option == "2"):
                print("Pedir sala de estudio")
                # aqui iria el codigo para pedir una sala de estudio, pero por ahora solo es un mensaje
            elif(option == "3"):
                print("Ver prestamos")
                # aqui iria el codigo para ver los prestamos, pero por ahora solo es un mensaje
            elif(option == "4"):
                print("Seccion de multas")
                # aqui iria el codigo para ver las multas, pero por ahora solo es un mensaje
            elif(option == "5"):
                print("Salir")
                break
            else:
                print("Opcion no valida, por favor ingrese una opcion valida")
        else:
            if(option == "1"):
                manage_books()
            elif(option == "2"):
                print("Gestionar Salas de estudio")
                # aqui iria el codigo para gestionar las salas de estudio, pero por ahora solo es un mensaje
            elif(option == "3"):
                print("Visualizar Prestamos")
                # aqui iria el codigo para visualizar los prestamos, pero por ahora solo es un mensaje
            elif(option == "4"):
                print("Gestionar Usuarios")
                # aqui iria el codigo para gestionar los usuarios, pero por ahora solo es un mensaje
            elif(option == "5"):
                print("Salir")
                break
            else:
                print("Opcion no valida, por favor ingrese una opcion valida")
    


def printMenu(userType = "student"):
    print("Bienvenido a la biblioteca")
    if(userType == "student"):
        print("1. Prestamo libro")
        print("2. Pedir sala de estudio")
        print("3. Ver prestamos")
        print("4. Seccion de multas")

    else:
        print("1. Gestionar Libros")
        print("2. Gestionar Salas de estudio")
        print("3. Visualizar Prestamos")
        print("4. Gestionar Usuarios")
    

    print("5. Salir")