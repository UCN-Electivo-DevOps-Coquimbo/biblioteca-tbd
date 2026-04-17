from entities.usuario import Usuario
from user_data import usuarios
    
def crear_usuario(rol_creador, nombre, rol, contraseña, list_lecturas):
    if rol_creador != "admin":
        print("Solo los administradores pueden crear usuarios.")
    
    nuevo_usuario = Usuario(nombre, rol, contraseña, list_lecturas)
    usuarios.append({
        "nombre": nuevo_usuario.nombre,
        "rol": nuevo_usuario.rol,
        "password": nuevo_usuario.contraseña,
        "lecturas": nuevo_usuario.lecturas
    })

    print("El usuario se ha creado exitosamente.")