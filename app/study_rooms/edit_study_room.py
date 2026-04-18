import json
import os

JSON_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'data',
    'study_rooms.json'
)

def edit_study_room(study_room_id, new_name=None, new_capacity=None):
    with open(JSON_FILE, 'r') as file:
        study_rooms = json.load(file)
    
    for study_room in study_rooms:
        if study_room['id'] == study_room_id:
            if new_name:
                study_room['name'] = new_name
            if new_capacity:
                study_room['capacity'] = new_capacity
                
    with open(JSON_FILE, 'w') as file:        
        json.dump(study_rooms, file)
        
def edit_study_room_flow():       
    study_rooms = {}
    print("Which study room do you want to edit?")
    print("------------ROOMS--------------")
    for study_room in json.load(open(JSON_FILE, 'r')):
        print(f"ID: {study_room['id']}, Name: {study_room['name']}, Capacity: {study_room['capacity']}")
        study_rooms[study_room['id']] = study_room
        
    while True:
        study_room_id_input = input("Enter the room ID: ")
        if not study_room_id_input:
            print("ID is required.")
        if int(study_room_id_input) not in study_rooms:
            print("ID not found.")
        else:
            break
    study_room_id = int(study_room_id_input)

    new_name = input("New name (leave blank to keep unchanged): ")

    while True:
        new_capacity_input = input("New capacity (leave blank to keep unchanged): ")
        if new_capacity_input and not new_capacity_input.isdigit():
            print("Capacity must be a number.")
        if new_capacity_input and int(new_capacity_input) <= 0:
            print("Capacity must be greater than 0.")
        else:
            break

    new_capacity = int(new_capacity_input) if new_capacity_input else None

    edit_study_room(study_room_id, new_name or None, new_capacity)
    print("Study room edited successfully.")