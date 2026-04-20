import utils as biblioteca_utils
from utils import DATA_PATH_USERS


def load_users():
    users_data = biblioteca_utils.load_json_data(DATA_PATH_USERS)
    if isinstance(users_data, dict):
        return users_data.get("users", [])
    return []


def load_room_loans():
    rooms = biblioteca_utils.load_json_data("app/data/study_rooms.json")
    if isinstance(rooms, list):
        return [room for room in rooms if not room.get("available", True)]
    return []


def get_column_widths(loans, users_dict):
    widths = {
        'room_id': len('Room ID'),
        'user_id': len('User ID'),
        'user': len('User'),
        'room': len('Room'),
        'capacity': len('Capacity')
    }
    
    for loan in loans:
        widths['room_id'] = max(widths['room_id'], len(str(loan['id'])))
        widths['user_id'] = max(widths['user_id'], len(str(loan['user_id'])))
        
        user = users_dict.get(loan['user_id'])
        user_name = user['name'] if user else 'User not found'
        widths['user'] = max(widths['user'], len(user_name))
        
        widths['room'] = max(widths['room'], len(loan['name']))
        widths['capacity'] = max(widths['capacity'], len(str(loan['capacity'])))
    
    return widths



def view_user_loans_admin(user_id, loans, users_dict):
    if not loans:
        print("No loans found.")
        return

    has_loans = False
    for loan in loans:
        if loan["user_id"] == user_id:
            has_loans = True
            print(f"Room ID: {loan['id']}")
            print(f"Room:    {loan['name']} (Capacity: {loan['capacity']})")
            print("-" * 50)

    if not has_loans:
        print("This user doesn't have room loans.\n")


def print_loans(loans, users_dict):
    if not loans:
        print("No loans found.")
        return

    widths = get_column_widths(loans, users_dict)
    
    header = f"{'Room ID':<{widths['room_id']}} | {'User ID':<{widths['user_id']}} | {'User':<{widths['user']}} | {'Room':<{widths['room']}} | {'Capacity':<{widths['capacity']}}"
    separator = "-" * len(header)
    
    print("\n" + "=" * len(header))
    print(header)
    print(separator)

    for loan in loans:
        user = users_dict.get(loan["user_id"])
        user_name = user["name"] if user else "User not found"

        print(f"{loan['id']:<{widths['room_id']}} | {loan['user_id']:<{widths['user_id']}} | {user_name:<{widths['user']}} | {loan['name']:<{widths['room']}} | {loan['capacity']:<{widths['capacity']}}")

    print(separator)


def search_loans_by_user_name(user_name, loans, users_dict):
    user_name = user_name.strip().lower()
    
    matching_user_ids = []
    for user_id, user in users_dict.items():
        if user_name in user["name"].lower():
            matching_user_ids.append(user_id)
    
    if not matching_user_ids:
        print("No users found with that name.")
        return
    
    result = [loan for loan in loans if loan["user_id"] in matching_user_ids]
    print_loans(result, users_dict)


def search_loans_by_room_name(room_name, loans, users_dict):
    room_name = room_name.strip().lower()
    result = [loan for loan in loans if room_name in loan["name"].strip().lower()]
    
    if not result:
        print("No rooms found with that name.")
        return

    print_loans(result, users_dict)
