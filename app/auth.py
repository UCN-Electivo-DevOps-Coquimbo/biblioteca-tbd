import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "users.json")


def _load_users():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_users(datos):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def login():
    print("\n--- Iniciar Sesión ---")
    email = input("Email: ").strip()
    password = input("Contraseña: ").strip()

    datos = _load_users()
    for usuario in datos["users"]:
        if usuario["email"] == email and usuario["password"] == password:
            print(f"\nBienvenido, {usuario['nombre']} ({usuario['rol']})")
            return usuario  

    print("\nEmail o contraseña incorrectos.")
    return None


def register():
    print("\n--- Registrar Usuario ---")
    nombre = input("Nombre completo: ").strip()
    rol = input("Ingrese rol (estudiante/bibliotecario): ").strip()
    email = nombre
    if rol == "estudiante":
        email += "@alumnos.ucn.cl"
    else:
        email += "@ucn.cl"

    password = input("Contraseña: ").strip()

    datos = _load_users()

    for usuario in datos["users"]:
        if usuario["email"] == email:
            print("\nEse email ya está registrado.")
            return None

    nuevo_id = max(u["id"] for u in datos["users"]) + 1
    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "email": email,
        "password": password,
        "rol": rol
    }

    datos["users"].append(nuevo_usuario)
    _save_users(datos)

    print(f"\nUsuario '{nombre}' registrado exitosamente.")
    return nuevo_usuario
