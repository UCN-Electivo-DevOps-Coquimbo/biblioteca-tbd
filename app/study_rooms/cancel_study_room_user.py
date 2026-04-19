import json
import os

JSON_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data',
    'study_rooms.json'
)

def translate_availability(available):
    return "Yes" if available else "No"


def cancel_study_room_user(study_room_id):
    with open(JSON_FILE, 'r') as file:
        study_rooms = json.load(file)

    room_found = False
    for study_room in study_rooms:
        if study_room['id'] == study_room_id:
            room_found = True
            if study_room.get('available', True):
                return "Room is already available"
            study_room['available'] = True
            break

    if not room_found:
        return "ID not found"

    with open(JSON_FILE, 'w') as file:
        json.dump(study_rooms, file, indent=2)

    return "Study room canceled successfully"


def cancel_study_room_flow():
    study_rooms = {}
    print("Which study room do you want to cancel?")
    print("------------ROOMS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        if study_room['available'] == False:
            print(f"ID: {study_room['id']}, Name: {study_room['name']}, Capacity: {study_room['capacity']}, Available: {translate_availability(study_room['available'])}")
            study_rooms[study_room['id']] = study_room

    if not study_rooms:
        print("No rooms to cancel.")
        return
    
    while True:
        study_room_id_input = input("Enter the room ID: ")
        if not study_room_id_input:
            print("ID is required.")
            continue
        try:
            study_room_id = int(study_room_id_input)
        except ValueError:
            print("ID must be a number.")
            continue
        if study_room_id not in study_rooms:
            print("ID not found.")
            continue
        break

    result = cancel_study_room_user(study_room_id)
    print(result)
