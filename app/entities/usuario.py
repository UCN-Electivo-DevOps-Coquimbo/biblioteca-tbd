class Usuario:
    def __init__(self, nombre, rol, contraseña, list_lecturas):
        self.nombre = nombre
        self.rol = rol # admin OR alumno
        self.constaseña = contraseña
        self.lecturas = list_lecturas
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Rol: {self.rol}, Contraseña: {self.constaseña}, Lecturas: {self.lecturas}"