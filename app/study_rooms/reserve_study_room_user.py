import json
import os

JSON_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data',
    'study_rooms.json'
)

def translate_availability(available):
    return "Yes" if available else "No"

def reserve_study_room_user(study_room_id):
    with open(JSON_FILE, 'r') as file:
        study_rooms = json.load(file)
    
    for study_room in study_rooms:
        if study_room['id'] == study_room_id:
            if not study_room.get('available', True):
                return "Room not available"
            study_room['available'] = False
                
    with open(JSON_FILE, 'w') as file:        
        json.dump(study_rooms, file)

def reserve_study_room_flow():
    study_rooms = {}
    print("Which study room do you want to reserve?")
    print("------------ROOMS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        if study_room['available'] == True:
            print(f"ID: {study_room['id']}, Name: {study_room['name']}, Capacity: {study_room['capacity']}, Available: {translate_availability(study_room['available'])}")
            study_rooms[study_room['id']] = study_room

    if not study_rooms:
        print("No rooms to cancel.")
        return
    
    while True:
        study_room_id_input = input("Enter the room ID: ")
        if not study_room_id_input:
            print("ID is required.")
        if int(study_room_id_input) not in study_rooms:
            print("ID not found.")
        else:
            break
    study_room_id = int(study_room_id_input)
    result = reserve_study_room_user(study_room_id)
    if result == "Room not available":
        print(result)
    else:
        print("Study room reserved successfully.")