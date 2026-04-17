from user_data import usuarios

def eliminar_usuario(rol_creador, nombre):
    if rol_creador != "admin":
        print("Solo los administradores pueden eliminar usuarios.")
        return
    
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            usuarios.remove(usuario)
            print(f"Usuario {nombre} eliminado correctamente.")
            return
    
    print(f"Usuario {nombre} no encontrado.")
    return