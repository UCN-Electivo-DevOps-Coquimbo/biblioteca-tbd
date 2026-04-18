def menu_multas():
    while True:
        print("\n=== Sección de Multas ===")
        print("Indique que desea hacer:")
        print("1. Ver multas")
        print("2. Pagar multa")
        print("3. Volver al menú principal")
        opcion = input("> ")
        if opcion == "1":
            ver_multas()
        elif opcion == "2":
            pagar_multa()
        elif opcion == "3":
            break
        else:
            print("Opción no válida, por favor ingrese una opción válida.")

def ver_multas(): 
    print("Ver multas")
    # placeholder hasta tener el codigo d visualizar multas del usuario


def pagar_multa():
    print("Pagar multa")
    # placeholder hasta tener el codigo para pagar las multas registradas del usuario

