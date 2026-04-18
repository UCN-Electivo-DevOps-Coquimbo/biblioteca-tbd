from services.get_book import solicitar_prestamo_libro

opciones_alumno = ["1", "2", "3", "4", "5"]
opciones_admin = ["1", "2", "3", "4", "5"]
def menu(userType = "alumno"):
    opcion = ""
    if(userType == "alumno"):
        opciones = opciones_alumno
    else:
        opciones = opciones_admin

    while(True):
        printMenu(userType)
        opcion = input("> ")
        if(userType == "alumno"):
            if(opcion == "1"):
                solicitar_prestamo_libro()

            elif(opcion == "2"):
                print("Pedir sala de estudio")
                # aqui iria el codigo para pedir una sala de estudio, pero por ahora solo es un mensaje
            elif(opcion == "3"):
                print("Ver prestamos")
                # aqui iria el codigo para ver los prestamos, pero por ahora solo es un mensaje
            elif(opcion == "4"):
                print("Seccion de multas")
                # aqui iria el codigo para ver las multas, pero por ahora solo es un mensaje
            elif(opcion == "5"):
                print("Salir")
                break
            else:
                print("Opcion no valida, por favor ingrese una opcion valida")
        else:
            if(opcion == "1"):
                print("Gestionar Libros")
                # aqui iria el codigo para gestionar los libros, pero por ahora solo es un mensaje
            elif(opcion == "2"):
                print("Gestionar Salas de estudio")
                # aqui iria el codigo para gestionar las salas de estudio, pero por ahora solo es un mensaje
            elif(opcion == "3"):
                print("Visualizar Prestamos")
                # aqui iria el codigo para visualizar los prestamos, pero por ahora solo es un mensaje
            elif(opcion == "4"):
                print("Gestionar Usuarios")
                # aqui iria el codigo para gestionar los usuarios, pero por ahora solo es un mensaje
            elif(opcion == "5"):
                print("Salir")
                break
            else:
                print("Opcion no valida, por favor ingrese una opcion valida")
    


def printMenu(userType = "alumno"):
    print("Bienvenido a la biblioteca")
    if(userType == "alumno"):
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