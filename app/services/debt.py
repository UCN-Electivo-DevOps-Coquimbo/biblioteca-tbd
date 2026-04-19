def debt_menu():
    while True:
        print("\n=== Debt Section ===")
        print("What do you want to do:")
        print("1. View debt")
        print("2. Pay off debts")
        print("3. Return to main menu")
        opcion = input("> ")
        if opcion == "1":
            ver_multas()
        elif opcion == "2":
            pagar_multa()
        elif opcion == "3":
            break
        else:
            print("Invalid option, please select a valid number.")

def ver_multas(): 
    print("View debt")
    # placeholder hasta tener el codigo d visualizar multas del usuario


def pagar_multa():
    print("Pay off debts")
    # placeholder hasta tener el codigo para pagar las multas registradas del usuario

