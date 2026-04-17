from user_data import usuarios

def get_usuario():
    nombre = ""
    
    while not nombre:
        nombre = input("Ingrese el nombre del usuario a buscar ('c' para cancelar): ")

        if nombre.lower() == "c":
            print("Búsqueda cancelada.")
            return None

        if not nombre:
            print("El nombre no puede estar vacío.")

    usuario = None

    for u in usuarios:
        if u["nombre"].lower() == nombre.lower():
            usuario = u
            break

    if usuario:
        print(f"\nUsuario encontrado:")
        print(f"  Nombre : {usuario['nombre']}")
        print(f"  Rol    : {usuario['rol']}")
        print(f"  Libros : ", end="")

        if usuario["lecturas"]:
            print()
            for libro in usuario["lecturas"]:
                print(f"    - {libro}")
        else:
            print("Sin lecturas registradas.")
    else:
        print(f"\nNo se encontró ningún usuario con el nombre '{nombre}'.")

    return usuario