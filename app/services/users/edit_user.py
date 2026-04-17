from user_data import usuarios
from ...utils import esOpcion

def edicion(tipo, nombre_objetivo, nuevo_dato):
    for u in usuarios:
        if u['nombre'] == nombre_objetivo:
            if tipo == 'nombre':
                u['nombre'] = nuevo_dato
            elif tipo == 'rol':
                u['rol'] = nuevo_dato
            elif tipo == 'contrasenia':
                u['password'] = nuevo_dato
            print(f"Campo {tipo} actualizado con éxito.")
            return
    print("Usuario no encontrado.")


def editar_usuario(nombre, rol_creador):
    if rol_creador != "admin":
        print("Solo los administradores pueden crear usuarios.")
        return

    print("="*30)
    opcion = ""
    while (not esOpcion(opcion, ["1", "2", "3"], int)):
        print("1. Editar Nombre")
        print("2. Editar Rol")
        print("3. Editar Contraseña")
        opcion = input("> ")
    
    opcion_int = int(opcion)

    if opcion_int == 1:
        nuevo = input("Ingrese nuevo nombre> ")
        edicion('nombre', nombre, nuevo)
    elif opcion_int == 2:
        nuevo = input("Ingrese nuevo rol> ")
        edicion('rol', nombre, nuevo)
    elif opcion_int == 3:
        nuevo = input("Ingrese nueva contraseña> ")
        edicion('contrasenia', nombre, nuevo)