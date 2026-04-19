from users.user_repository import get_users, save_users
from app.entities.user import User
from ..utils import esOpcion

def create_user(creator_role, name, email, password, role, reading_list=None):
    if creator_role != "admin":
        print("Access denied: Only administrators can create users.")
        return

    data = get_users()
    user_list = data["users"]

    new_id = user_list[-1]["id"] + 1 if user_list else 1
    
    new_user = User(new_id, name, email, password, role, reading_list or [])

    user_data = {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "password": new_user.password,
        "role": new_user.role,
        "reading_list": new_user.reading_list
    }

    user_list.append(user_data)
    save_users(data)
    print(f"User '{name}' has been created successfully.")

def delete_user(creator_role, target_name):
    if creator_role != "admin":
        print("Access denied: Only administrators can delete users.")
        return

    data = get_users()
    users = data["users"]
    
    original_count = len(users)
    data["users"] = [u for u in users if u["name"].lower() != target_name.lower()]

    if len(data["users"]) < original_count:
        save_users(data)
        print(f"User '{target_name}' deleted successfully.")
    else:
        print(f"User '{target_name}' not found.")

def update_user_field(target_name, field, new_value):
    """Internal helper to update specific fields in JSON"""
    data = get_users()
    found = False

    for u in data["users"]:
        if u['name'].lower() == target_name.lower():
            u[field] = new_value
            found = True
            break
    
    if found:
        save_users(data)
        print(f"Field '{field}' updated successfully.")
    else:
        print("User not found.")

def edit_user_menu(target_name, creator_role):
    if creator_role != "admin":
        print("Access denied: Only administrators can edit users.")
        return

    print(f"\n--- Editing User: {target_name} ---")
    option = ""
    while not esOpcion(option, ["1", "2", "3"], int):
        print("1. Edit Name\n2. Edit Role\n3. Edit Password")
        option = input("> ")
    
    choice = int(option)
    if choice == 1:
        update_user_field(target_name, 'name', input("New name: "))
    elif choice == 2:
        update_user_field(target_name, 'role', input("New role: "))
    elif choice == 3:
        update_user_field(target_name, 'password', input("New password: "))

def find_user():
    name_query = input("Enter username to search ('c' to cancel): ").strip()
    if name_query.lower() == "c": return None

    data = get_users()
    user = next((u for u in data["users"] if u["name"].lower() == name_query.lower()), None)

    if user:
        print(f"\nUser Found:")
        print(f"  ID       : {user['id']}")
        print(f"  Name     : {user['name']}")
        print(f"  Role     : {user['role']}")
        
        books = user.get("reading_list", [])
        if books:
            print("  Books    :")
            for book in books: print(f"    - {book}")
        else:
            print("  Books    : No books registered.")
    else:
        print(f"\nNo user found with the name '{name_query}'.")
    return user

def list_all_users():
    data = get_users()
    users = data.get("users", [])

    if not users:
        print("No registered users found.")
        return

    print("\n" + "="*30)
    print("      SYSTEM USER LIST")
    print("="*30)
    for u in users:
        print(f"Name: {u['name']} | Role: {u['role']}")
        books = u.get("reading_list", [])
        if books:
            print(f"Reading: {len(books)} book(s)")
        else:
            print("Reading: Empty")
        print("-" * 30)