from user_data import usuarios

def obtener_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for u in usuarios:
        print(f"Nombre: {u['nombre']}")
        print(f"Rol: {u['rol']}")

        if u['lecturas']:
            print("Lecturas:")
            for libro in u['lecturas']:
                print(f"  - {libro}") 
        else:
            print("Lecturas: Sin libros asignados")
            
        print("-" * 20)