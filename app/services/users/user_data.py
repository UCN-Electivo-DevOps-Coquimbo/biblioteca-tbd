from entities.libro import Libro 

usuarios = [
    {
        "nombre": "Ana García",
        "rol": "admin",
        "password": "hashed_password_123",
        "lecturas": [
            Libro("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 1967, "Realismo Mágico", True),
            Libro("1984", "George Orwell", "Secker & Warburg", 1949, "Distopía", False)
        ]
    },
    {
        "nombre": "Roberto Martínez",
        "rol": "lector",
        "password": "secure_pass_456",
        "lecturas": [
            Libro("Fundación", "Isaac Asimov", "Gnome Press", 1951, "Ciencia Ficción", True)
        ]
    },
    {
        "nombre": "Lucía Torres",
        "rol": "lector",
        "password": "mypassword789",
        "lecturas": []
    }
]