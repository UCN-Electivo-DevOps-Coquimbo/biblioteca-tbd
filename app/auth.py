import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "users.json")


def _load_users():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_users(data):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def login():
    print("\n--- Log in ---")
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    data = _load_users()
    for user in data["users"]:
        if user["email"] == email and user["password"] == password:
            print(f"\Welcome, {user['name']} ({user['rol']})")
            return user  

    print("\nEmail or password wrong.")
    return None


def register():
    print("\n--- Register User ---")
    name = input("Full name: ").strip()
    rol = input("Input rol (student/library servant): ").strip()
    email = name
    if rol == "student":
        email += "@alumnos.ucn.cl"
    else:
        email += "@ucn.cl"

    password = input("Password: ").strip()

    data = _load_users()

    for user in data["users"]:
        if user["email"] == email:
            print("\nThis email address already exist.")
            return None

    new_id = max(u["id"] for u in data["users"]) + 1
    new_user = {
        "id": new_id,
        "name": name,
        "email": email,
        "password": password,
        "rol": rol
    }

    data["users"].append(new_user)
    _save_users(data)

    print(f"\nUser '{name}' successful register.")
    return new_user
